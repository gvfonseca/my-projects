package com.ece420.lab6;

import android.content.pm.ActivityInfo;
import android.graphics.BitmapFactory;
import android.hardware.Camera;
import android.hardware.Camera.PreviewCallback;
import android.graphics.Bitmap;
import android.graphics.Canvas;
import android.graphics.Matrix;
import android.graphics.PixelFormat;
import android.graphics.Rect;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
// import android.util.Log;
import android.view.SurfaceHolder;
import android.view.SurfaceView;
import android.view.WindowManager;
import android.widget.TextView;

import android.graphics.Color;
import android.content.res.Resources;

import java.io.IOException;
import java.lang.Math;
// import java.util.List;

class cluster {
    public int centroid;
    public float weight;
}

public class CameraActivity extends AppCompatActivity implements SurfaceHolder.Callback{

    // UI Variable
    private SurfaceView surfaceView;
    private SurfaceHolder surfaceHolder;
    private SurfaceView surfaceView2;
    private SurfaceHolder surfaceHolder2;
    private TextView textHelper;
    // Camera Variable
    private Camera camera;
    boolean previewing = false;
    private int width = 320;
    private int height = 240;

    // Kernels
    private double[][] boxBlur = new double[][] {{1./9, 1./9, 1./9}, {1./9, 1./9, 1./9}, {1./9, 1./9, 1./9}};
    private double[][] boxBlur55 = new double[][] {{1./25, 1./25, 1./25, 1./25, 1./25}, {1./25, 1./25, 1./25, 1./25, 1./25}, {1./25, 1./25, 1./25, 1./25, 1./25}, {1./25, 1./25, 1./25, 1./25, 1./25}, {1./25, 1./25, 1./25, 1./25, 1./25}};

    private static final int clustersPerPixel = 5;
    private static final int defaultClusterVal = 128;
    private static final int threshold = 20;
    private static final int L = 100;
    private static final float fgmin = 0.5f;
    private cluster[][][] clusters = new cluster[height][width][clustersPerPixel];

    Bitmap bm;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        getWindow().setFormat(PixelFormat.UNKNOWN);
        getWindow().addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON);
        setContentView(R.layout.activity_camera);
        super.setRequestedOrientation (ActivityInfo.SCREEN_ORIENTATION_PORTRAIT);

        // Modify UI Text
        textHelper = (TextView) findViewById(R.id.Helper);
        textHelper.setText("Foreground/Background Segmented Feed");

        // Setup Surface View handler
        surfaceView = (SurfaceView)findViewById(R.id.ViewOrigin);
        surfaceHolder = surfaceView.getHolder();
        surfaceHolder.addCallback(this);
        surfaceHolder.setType(SurfaceHolder.SURFACE_TYPE_PUSH_BUFFERS);
        surfaceView2 = (SurfaceView)findViewById(R.id.ViewHisteq);
        surfaceHolder2 = surfaceView2.getHolder();

        // Cluster initialization
        initClusters();

        Resources res = getResources();
        if (MainActivity.imageFlag == 0) {
            bm = BitmapFactory.decodeResource(res, R.drawable.lake);
        } else if (MainActivity.imageFlag == 1) {
            bm = BitmapFactory.decodeResource(res, R.drawable.forest);
        } else {
            bm = BitmapFactory.decodeResource(res, R.drawable.beach);
        }
    }


    @Override
    public void surfaceChanged(SurfaceHolder holder, int format, int width, int height) {
        // Must have to override native method
        return;
    }

    @Override
    public void surfaceCreated(SurfaceHolder holder) {
        if(!previewing) {
            camera = Camera.open();
            if (camera != null) {
                try {
                    // Modify Camera Settings
                    Camera.Parameters parameters = camera.getParameters();
                    parameters.setPreviewSize(width, height);
                    // Following lines could log possible camera resolutions, including
                    // 2592x1944;1920x1080;1440x1080;1280x720;640x480;352x288;320x240;176x144;
                    // List<Camera.Size> sizes = parameters.getSupportedPictureSizes();
                    // for(int i=0; i<sizes.size(); i++) {
                    //     int height = sizes.get(i).height;
                    //     int width = sizes.get(i).width;
                    //     Log.d("size: ", Integer.toString(width) + ";" + Integer.toString(height));
                    // }
                    // Disable camera auto focus
                    parameters.setExposureCompensation(2);
                    parameters.setAutoExposureLock(true);

                    camera.setParameters(parameters);
                    camera.setDisplayOrientation(90);
                    camera.setPreviewDisplay(surfaceHolder);
                    camera.setPreviewCallback(new PreviewCallback() {
                        public void onPreviewFrame(byte[] data, Camera camera)
                        {
                            // Lock canvas
                            Canvas canvas = surfaceHolder2.lockCanvas(null);
                            // Where Callback Happens, camera preview frame ready
                            onCameraFrame(canvas,data);
                            // Unlock canvas
                            surfaceHolder2.unlockCanvasAndPost(canvas);
                        }
                    });
                    camera.startPreview();
                    previewing = true;
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }

    @Override
    public void surfaceDestroyed(SurfaceHolder holder) {
        // Cleaning Up
        if (camera != null && previewing) {
            camera.stopPreview();
            camera.setPreviewCallback(null);
            camera.release();
            camera = null;
            previewing = false;
        }
    }

    // Camera Preview Frame Callback Function
    protected void onCameraFrame(Canvas canvas, byte[] data) {

        Matrix matrix = new Matrix();
        matrix.postRotate(90);
        int retData[];

        // Apply foreground/background segmentation
        if (MainActivity.convFlag == 0) {
            // Green screen background
            int[] locs = matchUpdate(data);
            int[] mask = classify(locs);
            int[] out = postprocessing(mask);
            int[] result = greenmask(out, data);
            retData = merge(result, result);
        } else {
            // Blurred background
            int[] blurred = conv2(data, width, height, boxBlur55);
            int[] locs = matchUpdate(data);
            int[] mask = classify(locs);
            int[] out = postprocessing(mask);
            int[] result = blurbg(out, data, blurred);
            retData = merge(result, result);
        }

        // Create ARGB Image, rotate and draw
        Bitmap bmp = Bitmap.createBitmap(retData, width, height, Bitmap.Config.ARGB_8888);
        bmp = Bitmap.createBitmap(bmp, 0, 0, bmp.getWidth(), bmp.getHeight(), matrix, true);
        canvas.drawBitmap(bmp, new Rect(0,0, height, width), new Rect(0,0, canvas.getWidth(), canvas.getHeight()),null);
    }

    // Helper function to convert YUV to RGB
    public int[] yuv2rgb(byte[] data){
        final int frameSize = width * height;
        int[] rgb = new int[frameSize];

        for (int j = 0, yp = 0; j < height; j++) {
            int uvp = frameSize + (j >> 1) * width, u = 0, v = 0;
            for (int i = 0; i < width; i++, yp++) {
                int y = (0xff & ((int) data[yp])) - 16;
                y = y<0? 0:y;

                if ((i & 1) == 0) {
                    v = (0xff & data[uvp++]) - 128;
                    u = (0xff & data[uvp++]) - 128;
                }

                int y1192 = 1192 * y;
                int r = (y1192 + 1634 * v);
                int g = (y1192 - 833 * v - 400 * u);
                int b = (y1192 + 2066 * u);

                r = r<0? 0:r;
                r = r>262143? 262143:r;
                g = g<0? 0:g;
                g = g>262143? 262143:g;
                b = b<0? 0:b;
                b = b>262143? 262143:b;

                rgb[yp] = 0xff000000 | ((r << 6) & 0xff0000) | ((g >> 2) & 0xff00) | ((b >> 10) & 0xff);
            }
        }
        return rgb;
    }

    // Helper function to merge the results and convert GrayScale to RGB
    public int[] merge(int[] xdata,int[] ydata){
        int size = height * width;
        int[] mergeData = new int[size];
        for(int i=0; i<size; i++)
        {
            int p = (int)Math.sqrt((xdata[i] * xdata[i] + ydata[i] * ydata[i]) / 2);
            mergeData[i] = 0xff000000 | p<<16 | p<<8 | p;
        }
        return mergeData;
    }

    public int[] conv2(byte[] data, int width, int height, double kernel[][]){
        // 0 is black and 255 is white.
        int size = height * width;
        int[] convData = new int[size];

        // Perform single channel 2D Convolution
        // Note that you only need to manipulate data[0:size] that corresponds to luminance
        // The rest data[size:data.length] is ignored since we only want grayscale output
        // *********************** START YOUR CODE HERE  **************************** //
        for (int i = 0; i < height; i++) {
            for (int j = 0; j < width; j++) {
                for (int m = 0; m < 5; m++) {
                    for (int n = 0; n < 5; n++) {
                        int h_eff = i + m - 2;
                        int p_eff = j + n - 2;
                        if (h_eff < 0 || p_eff < 0 || h_eff >= height || p_eff >= width) {
                            continue;
                        }
                        int loc = data[h_eff * width + p_eff] & 0xFF;
                        float res = (float) loc;
                        res *= kernel[m][n];
                        convData[i * width + j] += (int) res;
                    }
                }
            }
        }


        // *********************** End YOUR CODE HERE  **************************** //
        return convData;
    }

    private void initClusters() {
        // This goes in onCreate
        for (int i = 0; i < height; i++) {
            for (int j = 0; j < width; j++) {
                for (int k = 0; k < clustersPerPixel; k++) {
                    clusters[i][j][k] = new cluster();
                    clusters[i][j][k].centroid = defaultClusterVal;
                    clusters[i][j][k].weight = 1 / ((float) clustersPerPixel);
                }
            }
        }
    }
    public int[] matchUpdate(byte[] data) {
        int size = width * height;
        int[] locs = new int[size];
        for (int i = 0; i < height; i++) {
            for (int j = 0; j < width; j++) {
                int pixel_val = data[i * width + j] & 0xFF;
                int min_distance = Integer.MAX_VALUE;
                int matched = -1;

                // Find best matching cluster for current pixel
                for (int k = 0; k < clustersPerPixel; k++) {
                    int dist = Math.abs(pixel_val - clusters[i][j][k].centroid);
                    if (dist < min_distance) {
                        min_distance = dist;
                        matched = k;
                    }
                }

                // Store index of matched cluster
                locs[i * width + j] = matched;

                // Update
                if (min_distance < threshold) {
                    // Acceptable match; update clusters accordingly
                    for (int k = 0; k < clustersPerPixel; k++) {
                        if (k == matched) {
                            clusters[i][j][k].weight += (1.0 / L) * (1 - clusters[i][j][k].weight);
                        } else {
                            clusters[i][j][k].weight -= (1.0 / L) * clusters[i][j][k].weight;
                        }
                    }
                    clusters[i][j][matched].centroid = (int) (clusters[i][j][matched].centroid + (1.0 / L) * (pixel_val - clusters[i][j][matched].centroid));
                } else {
                    // Find cluster with smallest weight and replace it
                    int smallest_weight_idx = 0;
                    for (int k = 1; k < clustersPerPixel; k++) {
                        if (clusters[i][j][k].weight < clusters[i][j][smallest_weight_idx].weight) {
                            smallest_weight_idx = k;
                        }
                    }
                    clusters[i][j][smallest_weight_idx].centroid = pixel_val;
                    clusters[i][j][smallest_weight_idx].weight = 1.0f / L;
                }

                // Normalize weights
                float sum = 0;
                for (int k = 0; k < clustersPerPixel; k++) {
                    sum += clusters[i][j][k].weight;
                }
                for (int k = 0; k < clustersPerPixel; k++) {
                    clusters[i][j][k].weight /= sum;
                }
            }
        }
        return locs;
    }
    public int[] classify(int[] locs) {
        // 0 is black and 255 is white.
        int size = height * width;
        int[] mask = new int[size];

        // Perform single channel 2D Convolution
        // Note that you only need to manipulate data[0:size] that corresponds to luminance
        // The rest data[size:data.length] is ignored since we only want grayscale output
        // *********************** START YOUR CODE HERE  **************************** //
        for (int i = 0; i < height; i++) {
            for (int j = 0; j < width; j++) {
                float hwSum = 0.0f;
                int matched = locs[i * width + j];
                if (matched < 0 || matched >= clustersPerPixel) {
                    // Error
                    continue;
                }
                for (int k = 0; k < clustersPerPixel; k++) {
                    if (clusters[i][j][k].weight > clusters[i][j][matched].weight) {
                        hwSum += clusters[i][j][k].weight;
                    }
                }

                if (hwSum > fgmin) {
                    mask[i * width + j] = 255;
                } else {
                    mask[i * width + j] = 0;
                }
            }
        }
        // *********************** End YOUR CODE HERE  **************************** //
        return mask;
    }

    public int[] postprocessing(int[] data) {
        // open, close
        data = applyMorphologicalOpen(data, 2);
//        data = applyMorphologicalClose(data, 3);
        return data;
    }
    public int[] applyMorphologicalOpen(int[] image, int kernelSize) {
        // Apply erosion followed by dilation
        image = applyErosion(image, kernelSize);
        image = applyDilation(image, kernelSize);

        return image;
    }

    public int[] applyMorphologicalClose(int[] image, int kernelSize) {
        // Apply erosion followed by dilation
        image = applyDilation(image, kernelSize);
        image = applyErosion(image, kernelSize);

        return image;
    }

    private int[] applyErosion(int[] image, int kernelSize) {
        int[] result = new int[width * height];

        int halfKernel = kernelSize / 2;

        for (int i = halfKernel; i < height - halfKernel; i++) {
            for (int j = halfKernel; j < width - halfKernel; j++) {
                int minVal = Integer.MAX_VALUE;

                for (int k = -halfKernel; k <= halfKernel; k++) {
                    for (int l = -halfKernel; l <= halfKernel; l++) {
                        int index = (i + k) * width + (j + l);
                        int pixelVal = image[index];
                        if (pixelVal < minVal) {
                            minVal = pixelVal;
                        }
                    }
                }

                int index = i * width + j;
                result[index] = minVal;
            }
        }

        return result;
    }

    private int[] applyDilation(int[] image, int kernelSize) {
        int[] result = new int[width * height];

        int halfKernel = kernelSize / 2;

        for (int i = halfKernel; i < height - halfKernel; i++) {
            for (int j = halfKernel; j < width - halfKernel; j++) {
                int maxVal = Integer.MIN_VALUE;

                for (int k = -halfKernel; k <= halfKernel; k++) {
                    for (int l = -halfKernel; l <= halfKernel; l++) {
                        int index = (i + k) * width + (j + l);
                        int pixelVal = image[index];
                        if (pixelVal > maxVal) {
                            maxVal = pixelVal;
                        }
                    }
                }

                int index = i * width + j;
                result[index] = maxVal;
            }
        }

        return result;
    }

    private int[] greenmask(int[] mask, byte[] data) {
        int[] result = new int[width * height];
        for (int i = 0; i < width * height; i++) {
            if (mask[i] != 0) {
                result[i] = data[i] & 0xFF;
            } else {
                // Set to the image
                int pixel = bm.getPixel(i / width, i % width);
                int alpha = Color.alpha(pixel);
                int red = Color.red(pixel);
                int green = Color.green(pixel);
                int blue = Color.blue(pixel);
                int gray = (int) (red * 0.299 + green * 0.587 + blue * 0.114);
                result[i] = gray;
            }
        }
        return result;
    }

    private int[] blurbg(int[] mask, byte[] data, int[] blurred) {
        int[] result = new int[width * height];
        for (int i = 0; i < width * height; i++) {
            if (mask[i] != 0) {
                // Set to the original image
                result[i] = data[i] & 0xFF;
            } else {
                // Set to the blurred image
                result[i] = blurred[i];
            }
        }
        return result;
    }
}

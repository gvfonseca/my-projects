package com.ece420.lab6;

import android.content.ContentUris;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.content.pm.ActivityInfo;
import android.Manifest;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.v4.content.ContextCompat;
import android.support.v4.app.ActivityCompat;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.view.WindowManager;
import android.widget.Button;
import android.widget.Spinner;
import android.widget.ArrayAdapter;
import android.widget.AdapterView;
import android.widget.ImageView;
import android.database.Cursor;
import android.provider.MediaStore;
import android.net.Uri;

public class MainActivity extends AppCompatActivity {

    // Flags to control app behavior
    public static int imageFlag = 0;
    public static int convFlag = 0;

    // UI Variables
    private Button sharpButton;
    private Button convButton;
    private Spinner dropdown;
    private ImageView imView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        getWindow().addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON);
        setContentView(R.layout.activity_main);
        super.setRequestedOrientation (ActivityInfo.SCREEN_ORIENTATION_PORTRAIT);

        // Request User Permission on Camera
        if(ContextCompat.checkSelfPermission(this, Manifest.permission.CAMERA) == PackageManager.PERMISSION_DENIED){
            ActivityCompat.requestPermissions(this, new String[] {Manifest.permission.CAMERA}, 1);}

        // Setup Button for Sharpening
        sharpButton = (Button) findViewById(R.id.sharpeButton);
        sharpButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(MainActivity.this, CameraActivity.class));
            }
        });

        imView = (ImageView) findViewById(R.id.imageview);

        // Setup Button for Convoution
        convButton = (Button) findViewById(R.id.convButton);
        convButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                convFlag = 1;
                startActivity(new Intent(MainActivity.this, CameraActivity.class));
            }
        });

        // get the spinner from the xml.
        dropdown = (Spinner) findViewById(R.id.spinner1);
        // create a list of items for the spinner.
        String[] items = new String[]{"Lake", "Forest", "Beach"};
        // create an adapter to describe how the items are displayed
        ArrayAdapter<String> adapter = new ArrayAdapter<>(this, android.R.layout.simple_spinner_dropdown_item, items);
        // set the spinners adapter to the previously created one.
        dropdown.setAdapter(adapter);

        // Add an OnItemSelectedListener to the spinner
        dropdown.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> parentView, View selectedItemView, int position, long id) {
                // Get the selected item from the spinner
                String selectedItem = items[position];

                // Check the selected item and set the flag variable accordingly
                if (selectedItem.equals("Lake")) {
                    // Set flag variable to indicate choice 1
                    imageFlag = 0;
                    imView.setImageResource(R.drawable.lake);
                } else if (selectedItem.equals("Forest")) {
                    // Set flag variable to indicate choice 2
                    imageFlag = 1;
                    imView.setImageResource(R.drawable.forest);
                } else if (selectedItem.equals("Beach")) {
                    // Set flag variable to indicate choice three
                    imageFlag = 2;
                    imView.setImageResource(R.drawable.beach);
                }
            }

            @Override
            public void onNothingSelected(AdapterView<?> parentView) {
                // Do nothing if nothing is selected
            }
        });
    }

    @Override
    protected void onResume(){
        super.setRequestedOrientation (ActivityInfo.SCREEN_ORIENTATION_PORTRAIT);
        super.onResume();
    }

}

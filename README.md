
<img src = "https://github.com/user-attachments/assets/73b76be8-7f97-495e-b71f-5c984336e823" width="20%" height="20%">


# CAPYMERA✨
Finally, we can be CAPYBARAs🦫  <br> 
 <br> This is a recording program. It also offers a CAPYBARA filter.  <br> Feel free to be a CAPYBARA!

<br><br>

## **Basic Features**

### **1. Capture Video from Camera (cv.VideoCapture)**

```python
cap = cv2.VideoCapture(0)
```

- Opens the default camera (0) 

<br><br>

### **2. Record Video from Camera (cv.VideoWriter)**

```python
# Define codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (frame_width, frame_height))
```

- Uses the **XVID codec** to record a video (`output.avi`).
- Captures at **20 FPS** and matches the camera's resolution.

<br><br>


### **3. Recording Mode**
  <img src = "https://github.com/user-attachments/assets/9154cb61-c415-4fc5-b22b-be53956912c1" width="40%" height="40%">
  <img src = "https://github.com/user-attachments/assets/130c31f7-6f64-48ce-a036-d26f1cfebb36" width="40%" height="40%">

  ```python
     if recording:
        out.write(frame)
        cv2.putText(display_frame, 'Recording...', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (10, 10, 200), 2)
    else:
        cv2.putText(display_frame, 'Ready to Record', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (25, 200, 50), 2)

    # Show frame
    cv2.imshow('Video Recorder', display_frame)
```

- **On**: Displays **"Recording..."** in **red** text.                   

- **Off**: Displays **"Ready to Record"** in **green** text.

    
<br><br>


### **4. Key Events & Controls**

| Key | Action |
| --- | --- |
| `Space` | Toggle recording ON/OFF |
| `ESC` | Exit the program |
| `F` | Toggle the Capybara Filter ON/OFF |

 ```python
display_frame = frame.copy()
    cv2.putText(display_frame, 'Record: Space | Exit: ESC | Filter: F', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
```
<br><br>

_Using `disply_frame`, of course these letters are not recorded!_

<br><br>
<br><br>




## **Capybara Filter 🦫**
<img src = "https://github.com/user-attachments/assets/9a7ddfa7-3ad4-4035-a32c-2bbc42f068c5" width="20%" height="20%">
<img src = "https://github.com/user-attachments/assets/efa62335-eb93-410e-a11e-93d24579bf17" width="40%" height="40%">
<img src = "https://github.com/user-attachments/assets/9a7ddfa7-3ad4-4035-a32c-2bbc42f068c5" width="20%" height="20%">



The filter can be **toggled ON/OFF** with the `F` key.

<br><br>


### **Face Detection & Mask Application**

- The program detects faces using the **Haar Cascade Classifier** (`haarcascade_frontalface_default.xml`).
   ```python
   haar_cascade_path = 'haarcascade_frontalface_default.xml'
   ...
   face_cascade = cv2.CascadeClassifier(haar_cascade_path)
   ...
   faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(50, 50))
   ```
  <br>
  
- When a face is detected, a **Capybara mask (`capy.png`)** is applied over the face.
   ```python
    if filter_enabled:
            overlay_image(frame, filter_img, x - int(w * 0.1), y - int(h * 0.4), int(w * 1.4), int(h * 1.5))
   ```
    - The **filter size** adjusts dynamically based on the detected face size.

  <br>
  
- **Smoothing Algorithm**:
    
    ```python
    face_history = deque(maxlen=10)
    ```
    ```python
    # Store face positions for smoothing
    face_history.append((x, y, w, h))
    
    # Compute moving average of the last 10 frames
    x = int(np.mean([pos[0] for pos in face_history]))
    y = int(np.mean([pos[1] for pos in face_history]))
    w = int(np.mean([pos[2] for pos in face_history]))
    h = int(np.mean([pos[3] for pos in face_history]))
    ```
    
    - Uses a **moving average** of the last 10 face positions to reduce trembling and improve stability.
    - Ensures smooth filter movement across frames.



<br><br>



# **Update**  


## **ver 2.0: Added Otter Filter** 
Due to the popularity of the **Capybara filter**, we have now added an **Otter filter**!🦦  
<img src =  "https://github.com/user-attachments/assets/055545f9-e943-4f9d-8ce7-523f51fc8ccf" width="20%" height="20%">
<img src = "https://github.com/user-attachments/assets/25f6e949-ec29-47e5-ade2-6375f066a645" width="40%" height="40%">
<img src = "https://github.com/user-attachments/assets/055545f9-e943-4f9d-8ce7-523f51fc8ccf" width="20%" height="20%">

_Plus, I resized the images' location to fit on a face_

<br><br>


### **1. Filter Status Display**  

added a text to display the **current filter status**.  

```python
if filter_enabled:
    cv2.putText(display_frame, f'Filter: {selected_filter.upper()}',
                (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
else:
    cv2.putText(display_frame, 'Filter: OFF',
                (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (100, 100, 100), 2)
```
- **active**: "Filter: CAPY" or "Filter: OTTER"
- **not active**: "Filter: OFF"  

<br><br>

### **2. New Key Bindings**  

| Key | Action |
|------|--------|
| `C` | Toggle the **Capybara** Filter ON |
| `O` | Toggle the **Otter** Filter ON |

<br><be>



---

*For Computer Vision*

<br>



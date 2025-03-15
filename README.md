
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

Opens the default camera (0) 

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

- **On**: Displays **"Recording..."** in **red** text.                   

- **Off**: Displays **"Ready to Record"** in **green** text.

    
_Of course these letters are not recorded!_
<br><br>


### **4. Key Events & Controls**

| Key | Action |
| --- | --- |
| `Space` | Toggle recording ON/OFF |
| `ESC` | Exit the program |
| `F` | Toggle the Capybara Filter ON/OFF |



<br><br>
<br><br>




## **Capybara Filter 🦫**
![capy](https://github.com/user-attachments/assets/9a7ddfa7-3ad4-4035-a32c-2bbc42f068c5)
![output](https://github.com/user-attachments/assets/efa62335-eb93-410e-a11e-93d24579bf17)

The filter can be **toggled ON/OFF** with the `F` key.

<br><br>


### **Face Detection & Mask Application**

- The program detects faces using the **Haar Cascade Classifier** (`haarcascade_frontalface_default.xml`).
- When a face is detected, a **Capybara mask (`capy.png`)** is applied over the face.
    - The **filter size** adjusts dynamically based on the detected face size.
- **Smoothing Algorithm**:
    
    ```python
    face_history = deque(maxlen=10)
    ```
    
    - Uses a **moving average** of the last 10 face positions to reduce trembling and improve stability.
    - Ensures smooth filter movement across frames.



<br><br>



---

*For Computer Vision *

<br>



#20191152 정세원 20221092 이준영
import numpy as np
import cv2
import os, sys

def main() :
    # check if input video, image, output video is inputed
    if len(sys.argv) != 4 :
        print("Wrong number value inputed!!")
    else :
        # set img by second input value in terminal
        img = cv2.imread(sys.argv[2])
        print(img.shape)
        # set video by first input value in terminal
        mv = cv2.VideoCapture(sys.argv[1])

        # make video fps, width, height variable to make recorder(result video)
        mv_fps = mv.get(cv2.CAP_PROP_FPS)
        mv_width = mv.get(cv2.CAP_PROP_FRAME_WIDTH)
        mv_height = mv.get(cv2.CAP_PROP_FRAME_HEIGHT)

        # check the video and image frame are same
        print(mv_fps,mv_height,mv_width)
        print(img.shape)

        # set the rgb range to erase green background of video
        low_range = np.array([0, 0, 0])
        high_range = np.array([255,243,255])

        # make result video file setting video, image frame value
        recorder = cv2.VideoWriter(sys.argv[3],cv2.VideoWriter_fourcc(*'mp4v'),
                            mv_fps,(int(mv_width),int(mv_height)))

        """
        make while loop to make chroma keying result video
        1. make background of image
        2. change video color rgb to hsv
        3. masking the video
        4. change 255 rgb value in masked video range in image
        5. write changed image at recorder(result video)
        """
        while mv.isOpened():
            ret,frame = mv.read()

            if frame is None :
                break
            else :
                # set result image img(beach.jpg)
                result = cv2.resize(img, (int(mv_width),int(mv_height)))

                #change video color rgb to hsv
                hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

                #masking the video
                mask = cv2.inRange(hsv, low_range, high_range)

                # change image to key
                result[mask == 255] = frame[mask==255]

                # write result image at recorder
                recorder.write(result)

                # if input (esc) the loop beak
                if cv2.waitKey(10) == 27 :
                    break

        mv.release()
        cv2.destroyAllWindows()

if __name__ == "__main__": # __ 
    main()
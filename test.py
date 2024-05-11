import pywhatkit as pw
import schedule
import time

# Function to send the WhatsApp message with image
def send_message_with_image(phone_number, image_path):
    pw.sendwhats_image(phone_number, image_path)
print("let's do it ")
# Replace the phone number with the desired recipient's number
phone_number = "+91 entre your phone number"

# Define image paths
image_path_1 = "images/image.jpg"
image_path_2 = "images/image2.jpg"  # Corrected path to image2.jpg

#image_path_3 = "images/{image one name with it's extention}"


# Schedule sending image1 at 12:52
schedule.every().day.at("13:05").do(send_message_with_image, phone_number, image_path_1)
print("it is working ")
# Schedule sending image2 at 12:55
schedule.every().day.at("13:08").do(send_message_with_image, phone_number, image_path_2)

#schedule.every().day.at("13:08").do(send_message_with_image, phone_number, image_path_3)


# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)

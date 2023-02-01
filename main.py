import pywhatkit
import pyautogui
from pynput.keyboard import Key, Controller

keyboard = Controller()

numbers = input('Введіть повний номер або нікнейм : ').split(" ")
msg = input('Введіть повідомлення : ')


def whatsapp_message(msg: str):
	try:
		for num in numbers:
			pywhatkit.sendwhatmsg_instantly(
				phone_no=num,
				message=msg,
				tab_close=True
			)
			pyautogui.click()
			keyboard.press(Key.enter)
			keyboard.release(Key.enter)
			print("Повідомлення надіслано!")
	except Exception as e:
		print(str(e))


if __name__ == "__main__":
	whatsapp_message(msg=msg)

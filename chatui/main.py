from uuid import uuid4
from nicegui import ui
from fastapi import FastAPI


app = FastAPI(title="Chat UI")

messages = []

@ui.refreshable
def chat_messages(own_id):
	for user_id, avatar, text in messages:
		ui.chat_message(
			avatar=avatar,
			text=text,
			sent=user_id==own_id,
		)

@ui.page("/")
def chat_page():
	def send():
		messages.append((user, avatar, text.value))
		chat_messages.refresh()
		text.value = ''

	user = str(uuid4())
	avatar= f'https://robohash.org/{user}?bgset=bg2'

	with ui.column().classes('w-full items-stretch'):
		chat_messages(user)

	with ui.footer().classes('bg-white'):
		with ui.row().classes('w-full items-center'):
			text = ui.input(placeholder='message') \
				.props('rounded outlined').classes('flex-grow') \
				.on('keydown.enter', send)

ui.run_with(app)

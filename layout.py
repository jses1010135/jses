#!/usr/bin/env python3
from nicegui import ui
from temp import templayout

@ ui.page('/')
def homepage():
    templayout()
    ui.label('home')
    with ui.card().classes('border border-green-400 w-full h-full justify-center'):
        with ui.column().classes('border border-red-400 w-full h-full justify-center'):
            ui.input(label='帳號').classes('w-full')
            ui.input(label='密碼').classes('w-full')
            ui.input(label='email').classes('w-full')
            ui.input(label='address').classes('w-full')
        with ui.row().classes('w-full h-full'):
            ui.button(text='新增',on_click=lambda: ui.navigate.to('/page1'))
            ui.button(text='修改',on_click=lambda: ui.navigate.to('/page2'))
            ui.space()
            ui.button(text='刪除',on_click=lambda: ui.navigate.to('/'))
    with ui.grid(columns='100px 100px auto auto').classes('w-full h-full border border-red-400'):
        ui.label('帳號')
        ui.label('密碼')
        ui.label('email')
        ui.label('address')
        
@ ui.page('/page1')
def page1():
    templayout()   
    ui.label('page1')    
@ ui.page('/page2')
def page2():
    templayout()
    ui.label('page2')
ui.run()
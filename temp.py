from nicegui import ui

def templayout():
    with ui.header().classes(replace='row items-center') as header:
        
        ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white')
        
           

    

    with ui.left_drawer().classes('bg-blue-100') as left_drawer:
        
        ui.label('Side menu')
        ui.button(text='home',on_click=lambda: ui.navigate.to('/'))
        ui.button(text='page1',on_click=lambda: ui.navigate.to('/page1'))
        ui.button(text='page2 ',on_click=lambda: ui.navigate.to('/page2'))
    
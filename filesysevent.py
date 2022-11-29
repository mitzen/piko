from watchdog.events import LoggingEventHandler

class FileEvent(LoggingEventHandler):
    def dispatch(self, event: any) -> None:
        if event.event_type == "created" and event.is_directory == False:
            print(f"Processig {event.src_path}")

def main():
  import os
  
  os.system("pip install -U scratchattach")
  
  import scratchattach as scratch3
  from scratchattach import Encoding
  import winsound
  
  events = scratch3.CloudEvents("669020072")
  
  @events.event
  def on_set(event): #Called when a cloud var is set
      print(f"{event.user}: {Encoding.decode(event.value)}")
      winsound.Beep(1000, 200)
  
  @events.event
  def on_del(event):
      print(f"{event.user} deleted variable {event.var}")
  
  @events.event
  def on_create(event):
      print(f"{event.user} created variable {event.var}")
  
  @events.event #Called when the event listener is ready
  def on_ready():
     print("Event listener ready!")
  
  events.start()


if __name__ == '__main__':
  main()


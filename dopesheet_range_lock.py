import nuke

def sync_frame_range():
    first_frame = nuke.root().firstFrame()
    last_frame = nuke.root().lastFrame()

    nuke.frame(first_frame)
    nuke.zoomToFitSelected() 

nuke.addOnCreate(sync_frame_range, nodeClass='Root')

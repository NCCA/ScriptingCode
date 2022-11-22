script = """
proc manipChanger()
{
  string $sel[] = `ls -sl`;
  if (`attributeExists "scaleManip" $sel[0]`) 
  {
    ScaleTool;
  }
  if (`attributeExists "rotateManip" $sel[0]`) 
  {
    RotateTool;
  }
  if (`attributeExists "moveManip" $sel[0]`) 
  {
    MoveTool;
  }
}    


int $jobId = `scriptJob -killWithScene -event "SelectionChanged" "manipChanger"`;
"""

nodeName = cmds.scriptNode(st=2, bs=script, n="manipUpdate", stp="mel")

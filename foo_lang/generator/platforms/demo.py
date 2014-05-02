# demo.py
# author: Christophe VG

# Demo Generator Platform implementation
# adds imports for application-specific and shared-with-manual functionality

from foo_lang.generator.platforms.moose import Moose

import codecanvas.instructions as code

class Demo(Moose):
  def setup(self, unit):
    super(Demo, self).setup(unit)

    code.Import("../lib/application").insert_after(unit.find("main_h"))
    unit.find("init").append(code.Import("../lib/init.c")).stick_top()
    unit.find("step").append(code.Import("../lib/application_step.c"))
    unit.find("event_loop").append(code.FunctionCall("report_metrics")).stick_bottom()

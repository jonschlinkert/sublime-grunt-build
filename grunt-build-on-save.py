import sublime, sublime_plugin,os

class BuildGruntOnSave(sublime_plugin.EventListener):

  def on_post_save(self, view):
    print 'BuildGruntOnSave: on_post_save'
    folder = view.window().folders()[0]
    os.chdir(folder)

    #let's see if project wants to be autobuilt.
    should_build = view.settings().get('build_on_save')
    if should_build == 1:
      view.window().run_command('exec',{'cmd':['grunt'],'working_dir':folder})
    else:
      print 'BuildGruntOnSave: Project not configured for build_on_save.  Try setting build_on_save in project settings'

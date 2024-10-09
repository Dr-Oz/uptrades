# Test task UpTrade


Task

You need to create a Django app that implements a tree menu, adhering to the following requirements:

 • The menu is implemented via a template tag.
 • Everything above the selected item is expanded. The first level of nesting under the selected item is also expanded.
 • The menu is stored in the database.
 • It can be edited in the standard Django admin panel.
 • The active menu item is determined based on the URL of the current page.
 • There can be multiple menus on the same page, identified by their names.
 • Clicking on a menu item navigates to the URL specified in it. The URL can be either explicitly defined or referenced through a named URL.
 • Rendering each menu should require exactly one database query.

The Django app should allow adding menus (one or more) to the database through the admin panel and rendering a menu by name on any desired page. For example: {% draw_menu 'main_menu' %}.

Only Django and the Python standard library should be used for this task.

Let me know if you need any further changes, but the translation is accurate and clear.

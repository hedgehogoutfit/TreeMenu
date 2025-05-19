from django import template
from menus.models import MenuItem
from collections import defaultdict

register = template.Library()

@register.inclusion_tag('menus/the_menu.html', takes_context=True)
def draw_menu(context, menu):
    request = context['request']
    current_path = request.path
    main_menu = f'<a href="/{menu.url}">{menu.name}</a>'
    if menu.url not in current_path:
        return {'menu': main_menu}
    else:

        menu_items = MenuItem.objects.select_related('parent').filter(menu=menu)

        items_dict = defaultdict(list)
        for item in menu_items:
            items_dict[item.parent].append(item)

        def render_html(parent=None):
            """Recursively renders menu items as HTML."""
            units = items_dict.get(parent, [])
            html = ''
            if units:
                html = "<ul>" + html

                for unit in units:
                    html += f"<li><a href='/{unit.url}'>{unit.name}</a>"   # this slash!
                    if unit.url in current_path:
                        html += render_html(unit)   # Recursively render children
                    html += f"</li>"
                html += f"</ul>"
            return html
        menu_items = render_html()
        return {'menu': main_menu, 'menu_items': menu_items}




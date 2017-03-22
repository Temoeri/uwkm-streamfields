from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField, RichTextField

from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel, \
        InlinePanel, PageChooserPanel, StreamFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

from wagtail.wagtailimages.blocks import ImageChooserBlock

from wagtail.wagtailforms.models import AbstractEmailForm, AbstractFormField

from .blocks import *

from .icon import IconChoiceBlock


spec_table_options = {
    'minSpareRows': 0,
    'startRows': 4,
    'startCols': 4,
    'colHeaders': False,
    'rowHeaders': False,
    'contextMenu': True,
    'editor': 'text',
    'stretchH': 'all',
    'height': 108,
    'language': 'nl',
    'renderer': 'text',
    'autoColumnSize': False,
}


STREAMFIELDS = StreamField(
    [('grid', blocks.ListBlock(
        GridBlock(),
        template = 'presentation/grid.html',
        icon='grip',))
    ,('tabellen', TableBlock(
        label='Tabellen',
        table_options=spec_table_options,
        template = 'presentation/table.html',))
    ,('citaten', blocks.ListBlock(
        QuoteBlock(),
        template = 'presentation/quotes.html',
        icon="openquote",))
    ,('koppen', blocks.ListBlock(
        HeaderBlock(),
        template = 'presentation/header.html',
        icon="title",))
    ,('tekst_velden', blocks.ListBlock(
        TextFieldBlock(),
        template = 'presentation/text_field.html',
        icon="doc-full",))
    ,('accordions', blocks.ListBlock(
        AccordionBlock(),
        template = 'presentation/accordion.html',
        icon='list-ol',))
    ,('tabs', blocks.ListBlock(
        TabBlock(),
        template = 'presentation/tab.html',
        icon='list-ol',))
    ,('afbeelding_met_tekst', blocks.ListBlock(
        BackgroundBlock(),
        template = 'presentation/background_with_text.html',
        icon='doc-full',))
    ,('gekleurde_blokken', blocks.ListBlock(
        ColoredTextBlock(),
        template = 'presentation/colored_block.html',
        icon="doc-full-inverse",))
    ,('gallerij', blocks.ListBlock(
        GalleryBlock(),
        template = 'presentation/gallery.html',
        icon='image',))
    ,('gallerij', blocks.ListBlock(
        GalleryBlock(),
        template = 'presentation/gallery.html',
        icon='image',))
    ,('afbeelding', GalleryBlock(
        template = 'presentation/image.html',
        icon='image'))
    ,('slogans', blocks.ListBlock(
        SloganBlock(),
        template = 'presentation/slogans.html',
        icon="list-ul",))
    ,('divider', blocks.ListBlock(
        DividerBlock(),
        template = 'presentation/devider.html',
        icon="horizontalrule",))   
    ,('html', blocks.ListBlock(
        HTMLBlock(),
        template = 'presentation/raw_html.html',
        icon="code",))
    ,('knop', blocks.ListBlock(
        ButtonBlock(),
        template = 'presentation/button.html',
        icon="tick",))
    ,('video', blocks.ListBlock(
        VideoBlock(),
        template = 'presentation/video.html',
        icon="media",))
    ,('icoon', blocks.ListBlock(
        IconBlock(),
        template = 'presentation/icon_block.html',
        icon="doc-empty",))
    ,('call_to_action', blocks.ListBlock(
        CallToActionBlock(),
        template = 'presentation/call_to_action.html',
        icon="tick",))
    ,('formulier', blocks.PageChooserBlock(
        target_model='presentation.FormPage',
        template = 'presentation/form.html',
        icon="form"))
    ,('diavoorstelling', blocks.ListBlock(
        SliderBlock(),
        template = 'presentation/slider.html',
        icon="image"))
    ],
    null = True,
    blank = True
)

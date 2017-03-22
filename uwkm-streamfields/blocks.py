from django import forms 
from django.db import models
from django.utils.translation import ugettext_lazy as _

from modelcluster.fields import ParentalKey

from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailforms.models import AbstractEmailForm, AbstractFormField

from .icons import IconChoiceBlock

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


class ColorChoiceBlock(blocks.ChoiceBlock):
    choices = [
        ('primary-cta',  'Primaire'),
        ('secondary-cta', 'Secundaire'),
        ('limegreen',    'Limegroen'),
        ('lightgray',   'Lichtgrijs'),
        ('midgray',   'Middengrijs'),
        ('darkgray',   'Dronkergrijs'),
        ('lightblue',   'Lichtblauw'),
    ]

class TextColorChoiceBlock(blocks.ChoiceBlock):
    choices = [
        ('white',  'Wit'),
        ('black',  'Zwart'),
    ]

class AlignChoiceBlock(blocks.ChoiceBlock):
    choices = [
        ('left', 'Links'),
        ('center', 'Midden'),
        ('right', 'Rechts'),
    ]

class GridChoiceBlock(blocks.ChoiceBlock):
    choices = [
        ('col-xs-12', '12'),
        ('col-xs-11', '11'),
        ('col-xs-10', '10'),
        ('col-xs-9', '9'),
        ('col-xs-8', '8'),
        ('col-xs-7', '7'),
        ('col-xs-6', '6'),
        ('col-xs-5', '5'),
        ('col-xs-4', '4'),
        ('col-xs-3', '3'),
        ('col-xs-2', '2'),
        ('col-xs-1', '1'),
    ]


class SliderBlock(blocks.StructBlock):
    image = ImageChooserBlock()

    name = blocks.CharBlock(
        label='Naam',
        max_length = 30,
        help_text = 'Verschijnt onderaan als navigatieknop.',
        required = True,
    )

    subtext = blocks.CharBlock(
        label='Subtekst',
        max_length = 35,
        help_text = 'Verschijnt onder de navigatieknop.',
        required = False,
    )

    button = blocks.BooleanBlock(
        label='Call to Action',
        default=False,
        help_text = 'Heeft een call to action knop.',
        required = False,
    )

    cta_text = blocks.CharBlock(
        label='CTA tekst',
        max_length = 20,
        required = False,
    )

    cta_pos  = blocks.ChoiceBlock(
		label = 'CTA Positie',
        choices = (
            ('left', _('Left')),
            ('right', _('Right'))
        ),
        required = False,
    )

    cta_color = ColorChoiceBlock(
        label = 'CTA achtergrondkleur',
        required = False,
    )

    cta_link_type = blocks.ChoiceBlock(
        label = 'CTA link type',
        choices = (
            ('wagtail', 'Wagtailpagina'),
            ('url', 'Handmatige url')
        ),
        required = False,
    )

    cta_page_link = blocks.PageChooserBlock(
        label = 'CTA wagtail link',
        can_choose_root = True,
        required= False,
    )

    cta_url = blocks.CharBlock(
        label='CTA url',
        max_length = 255,
        required = False,
    )

    class Meta:
        icon = 'image'

class SloganBlock(blocks.StructBlock):
    image = ImageChooserBlock()

    title = blocks.CharBlock(
        label = 'Naam',
        max_length = 30,
        help_text = 'Verschijnt onderaan als navigatieknop.',
        required = True,
    )

    text = blocks.TextBlock(
        label = 'Tekst',
        max_length = 120,
    )

class QuoteBlock(blocks.StructBlock):
    quote = blocks.TextBlock(
        label = 'Citaat',
        required = True,
        max_length = 150,
    )

    logo = ImageChooserBlock(required = False)

    name = blocks.CharBlock(
        label = 'Naam',
        max_length = 50,
        help_text = 'Naam van de persoon achter het citaat.',
    )

    company = blocks.CharBlock(
        label = 'Bedrijf',
        max_length = 50,
        help_text = 'Naam van het bedrijf achter het citaat.',
    )

    city = blocks.CharBlock(
        label = 'Plaats',
        max_length = 50,
        help_text = 'Plaats'
    )


class HeaderChoiceBlock(blocks.ChoiceBlock):
    choices = (
        ('h1', 'Kop een'),
        ('h2', 'Kop twee'),
        ('h3', 'Kop drie'),
        ('h4', 'Kop vier'),
        ('h5', 'Kop vijf'),
        ('h6', 'Kop zes'),
    )


class HeaderBlock(blocks.StructBlock):
    header = HeaderChoiceBlock(
        label = 'Kopgrootte',
        help_text = 'Grootte van de tekst.'
    )
    text = blocks.CharBlock(
        label = 'Tekst',
        max_length = 50,
        help_text = 'Tekst van de koptekst.',
    )


class AccordionBlock(blocks.StructBlock):
    title = blocks.CharBlock(
        label = 'Titel',
        max_length = 50,
        help_text = 'Tekst in de titel.',
    )
    content = blocks.RichTextBlock(
        label = 'Inhoud',
        help_text = 'Inhoud van de tab.',
    )


class TabBlock(blocks.StructBlock):
    title = blocks.CharBlock(
        label = 'Titel',
        max_length = 50,
        help_text = 'Tekst in de titel.',
    )
    content = blocks.RichTextBlock(
        label = 'Inhoud',
        help_text = 'Inhoud van de tab.',
    )


class TextFieldBlock(blocks.StructBlock):
    content = blocks.RichTextBlock(
        label = 'Tekstveld',
        help_text = 'Inhoud van het tekstveld.',
    )


class BackgroundBlock(blocks.StructBlock):
    background_image = ImageChooserBlock(
        label = 'Afbeelding',
        help_text = 'Het achtergrondplaatje van het blok.',
    )
    block_height = blocks.IntegerBlock(
        label = 'Hoogte',
        help_text = 'Hoogte van het blok in pixels.',
        min_value = 0,
        max_value = 999,
        default = 250,
    )
    text = blocks.RichTextBlock(
        label = 'Tekst',
        help_text = 'Tekst op de achtergrond.',
        required = False,
    )
    text_color = TextColorChoiceBlock(
        label = 'Kleur tekst',
        required = False,
    )
    align = AlignChoiceBlock(
        label = 'Uitlijning',
    )


class ColoredTextBlock(blocks.StructBlock):
    text = blocks.RichTextBlock(
        label = 'Tekst',
        required = False,
    )
    text_color = TextColorChoiceBlock(
        label = 'Kleur tekst',
        required = False,
    )
    background_color = ColorChoiceBlock(
        label = 'Achtergrondkleur',
        required = False,
    )


class GalleryBlock(blocks.StructBlock):
    image = ImageChooserBlock(
        label = 'Afbeelding',
        help_text = 'Een afbeelding in de gallerij.',
    )


class DividerBlock(blocks.StructBlock):
    border_color = blocks.ChoiceBlock(
        choices = [('primary', 'Primaire'),],
        label = 'Divider',
        help_text = 'Lijn kleur.',
    )


class HTMLBlock(blocks.StructBlock):
    raw_html = blocks.RawHTMLBlock(
        label = 'HTML blok',
        help_text = 'HTML blok',
    )


class ButtonBlock(blocks.StructBlock):
    button_class = ColorChoiceBlock(
        label = 'Opmaak',
        help_text = 'Opmaak van de knop.',
    )
    icon = IconChoiceBlock(
        label = 'Icoon',
        help_text = 'Icoon op de knop. (Font awesome)',
        required = False,
    )
    text = blocks.CharBlock(
        label = 'Tekst',
        max_length = 50,
        help_text = 'Tekst op de knop.',
    )
    width = blocks.ChoiceBlock(
        label = 'Breedte',
        choices = [
            (' ', 'Automatisch'), ('btn-block', '100%'),
        ]
    )
    link = blocks.PageChooserBlock(
        label = 'Link',
        can_choose_root = True,
        required= False,
    )
    ext_link = blocks.CharBlock(
        label='Externe link',
        max_length = 255,
        required = False,
    )

class VideoBlock(blocks.StructBlock):
    video_id = blocks.CharBlock(
        label = 'Video',
        max_length = 11,
        help_text = 'YouTube video code/id.',
    )

class IconBlock(blocks.StructBlock):
    icon = IconChoiceBlock(
        label = 'Icoon',
        help_text = 'Icoon. (Font awesome)',
    )
    text = blocks.RichTextBlock(
        label = 'Tekst',
        help_text = 'Tekst in het blok.',
    )

class CallToActionBlock(blocks.StructBlock):
    text = blocks.RichTextBlock(
        label = 'Tekst',
        help_text = 'Tekst in het blok.',
    )
    button = ButtonBlock()


class GridBlock(blocks.StructBlock):
    grid = GridChoiceBlock(
        label = 'Breedte kolom',
        help_text = 'De breedte kolommen (12 breedste, 1 smalste).',
    )
    content = blocks.StreamBlock(
        [('tabellen', TableBlock(
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
            icon="search",))
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
            template = 'presentation/form.html',
            icon="form"))
        ,('diavoorstelling', blocks.ListBlock(
            SliderBlock(),
            template = 'presentation/slider.html',
            icon="image"))
        ],
    )

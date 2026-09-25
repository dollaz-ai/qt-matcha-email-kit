# Design system

## Visual direction

Blend everyday cream and bright QT. Use one dominant accent per email. Broad, shallow waves connect large color fields; the small hand-drawn illustrations bring character without competing with the product. Preserve plenty of readable cream areas. Avoid rainbow gradients or variety-pack artwork.

## Palette

| Token | Hex | Use |
|---|---|---|
| Forest ink | `#2E4B21` | Body/headline ink; occasional full green section |
| Everyday cream | `#F9F8F1` | Main background, cards, light text on green |
| Strawberry pink | `#F5B1CB` | Welcome hero, strawberry moments |
| QT lime | `#C5E748` | Primary action, small highlights |
| Pale lime | `#E9F3BE` | Supporting panels and footer |
| White peach | `#FFD0B3` | Peach flavor labels / accents |
| Lemon yuzu | `#F4DF85` | Yuzu flavor labels / accents |

Use green text on the light palette and cream text on green. Avoid white text on pink, peach, lime or yellow for essential information.

## Type

- Headlines: **Bricolage Grotesque ExtraBold / 800**. Welcome H1 is 44 px desktop, 36 px mobile, line height 1.1. Supporting H2 is 28 px desktop / 26 px mobile.
- Body and buttons: **Figtree**, regular 400 and bold 700; semibold 600 is also installed. Body is 17 px desktop / 16 px mobile, line height 1.5.
- Labels: Figtree 11–13 px bold, modest 1–1.5 px tracking, short uppercase text.
- Supporting copy: 13–14 px. Footer: 12 px. The existing regulatory disclaimer is 11 px; review its readability before launch.
- Coupon code: the current template intentionally uses a 30 px monospace code for easy recognition/copying; this is an exception to the brand type system.
- Font sources: [Bricolage Grotesque](https://fonts.google.com/specimen/Bricolage+Grotesque), [Figtree](https://fonts.google.com/specimen/Figtree). Install through Klaviyo’s font library. Font binaries are not bundled here.
- Fallback: Arial, sans-serif. Custom fonts are not guaranteed in every inbox. Check both actual fonts and fallback rendering. Keep essential text editable. If a future decorative headline is exported as an image, give it equivalent alt text and keep the offer/action in live text.

## Layout and spacing

The implemented template has a **600 px** email body, fluid below that width. Figma references include 600 px and 375 px versions.

- Desktop text side padding: 32 px. Recommended mobile side padding: 20–24 px; verify native mobile overrides rather than assuming inheritance.
- Section padding: generally 24–32 px; within a group, 8–16 px.
- Primary button: green bold text on lime, 30 px radius; target at least 44 px tap height.
- Coupon card: cream on pink, 20 px rounded corners, 20 px vertical / 16 px horizontal internal padding.
- Wordmark: 210 px displayed width in Welcome 1.
- Welcome doodle: 88 px display width; typical decorative range 64–104 px. Never stretch a small doodle to full mobile width.
- Wave: 600 × 48 display pixels (source 1200 × 96). Full width, zero block/inner padding. Keep text in its own padded block; never lay text over the divider.
- Product moment: the current three-packet image displays at 360 px wide. Large blank space inside an image is separate from block padding—crop a duplicate asset if needed, preserving original proportions.

## Illustration grammar

160 × 160 source coordinate space, forest-green rounded strokes, approximately 3 px stroke at source size, small flat palette fills. Maintain aspect ratio and consistent line weight. Do not substitute emoji for icons: platform rendering changes their appearance. Use one lead doodle per email, with optional smaller supporting art. Never redraw or distort packet print.

## Reusable section structure

1. Wordmark + short status pill.
2. Small occasion illustration + one clear headline.
3. Main message or offer card + primary CTA.
4. Product/lifestyle moment (optional; use a relevant flavor).
5. Supporting story/ritual module; green works well here.
6. Helpful next step or sign-off.
7. Appropriate service or marketing footer.

Transaction emails prioritize order/tracking facts; campaigns prioritize a single story and action. Do not force every section into every email.

## Signature QT wave sections — use selectively

The soft, squiggly color-field edges are a signature part of this email system, alongside the typography and drawings. Carry them into selected sections of future emails, even when an earlier Figma concept shows straight edges. **Do not add a wave between every block or to every email.**

Use a wave to mark a meaningful change: a bright opening flowing into cream, a product moment flowing into a green ritual/story section, or that green section flowing back into cream. These are full-width section edges, not thin squiggles placed behind text.

- In most marketing emails, start with one or two wave transitions. A longer email can use three when they define clear sections, as Welcome 1 does.
- Keep straight edges and whitespace within a section: between headline and body, around a coupon card, between product details and a button, and in the footer.
- Short personal notes can use no waves. Order and shipping emails should prioritize clear information; one decorative hero transition is optional, while order tables, totals and tracking details stay clean.
- Never overlap text, buttons, packet imagery or important details with a wave. Give adjacent text its normal section padding; do not add tall empty sections just to accommodate decoration.

### Included transitions

| Divider | Placement | Asset |
|---|---|---|
| Pink → cream | Bottom of a pink welcome or campaign hero | [PNG](../assets/dividers/pink-cream.png) |
| Cream → green | Top of a green ritual / product-story section | [PNG](../assets/dividers/cream-green.png) |
| Green → cream | Bottom of that green section | [PNG](../assets/dividers/green-cream.png) |

Use the supplied PNG divider as a native image block, 600 × 48 px on desktop, scaling proportionally on mobile, with zero block and inner padding. Match the exact background colors above and below it. If a peach or yuzu campaign needs its own transition, export a matching recolored divider; do not place the pink divider against a peach background.

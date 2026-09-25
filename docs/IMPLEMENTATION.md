# From this pack to Klaviyo and Shopify

## Klaviyo: recommended editable workflow

1. Open the approved Soft Waves template or duplicate the current Welcome 1 email. Work in draft.
2. Confirm fonts in the editor library: Bricolage Grotesque 400/700/800 and Figtree 400/600/700, with Arial fallback. They were added to the QT account on September 25, 2026.
3. Build with native image, text and button blocks. Use Bricolage 800 for H1/H2 and Figtree for text/buttons. Keep coupon codes, product facts, offers and CTAs as live text.
4. Upload PNG illustrations and wave dividers from this pack to Klaviyo’s image library. Upload JPEG lifestyle images. Preserve the SVGs as editable masters, not as the default email image format.
5. Set wave blocks to full width with zero padding. Disable full-width mobile stretching for wordmarks and small doodles; retain responsive scaling for full-width photos.
6. Save shared header/footer/divider groups as universal content only when you intend edits to propagate to all linked usages. Duplicate occasion-specific sections.
7. Apply the finished template to the intended draft flow message. Klaviyo copies templates when assigning them—later edits to a standalone template do not automatically update an already-assigned message.
8. Configure real destinations and dynamic content, then preview desktop/mobile and test the fallback fonts. Have an authorized team member send inbox tests and approve activation.

## Files and portability

`templates/welcome-1.html` is the current Klaviyo export with account-hosted asset URLs and Klaviyo footer tags. It can be used as a custom HTML reference, but importing it as HTML does not recreate native drag-and-drop blocks.

`templates/welcome-1.klaviyo-definition.json` is the structured DND definition. It contains non-secret QT account asset IDs. Developers can use it with Klaviyo’s DND Templates API. For a new template, strip server-assigned `id`, `data_id`, and `template_id` keys, upload the included images into the destination account and replace `asset_id` values. No API credentials are included. Use the supplied asset map to identify images. Do not paste this JSON into the HTML editor.

`templates/welcome-1-preview.html` is a local visual reference, with bundled image paths and Google font loading. Its footer links are placeholders. **Do not upload or send the preview file.** Use the actual Klaviyo draft or adapt the source template.

Fonts may use fallback type in unsupported inboxes. PNG/JPEG assets avoid depending on SVG rendering inside email clients. Keep images as supporting content, so the message remains useful if images are blocked.

## Shopify: service notifications

Use the order/shipping reference images to style Shopify’s native notification templates. Retain Shopify’s existing Liquid variables, item loops, payment/tax details, order-status link and fulfillment/tracking logic. Do not paste a Klaviyo template or Klaviyo tags into Shopify notifications. Build and test with representative sample orders, including multiple items and partial fulfillment. Avoid enabling duplicate confirmations across Shopify and Klaviyo.

## Sources

- [Klaviyo custom fonts](https://help.klaviyo.com/hc/en-us/articles/4412748537627)
- [Klaviyo universal content](https://help.klaviyo.com/hc/en-us/articles/115005413888)
- [Klaviyo image guidance](https://help.klaviyo.com/hc/en-us/articles/4407911841435)
- [Klaviyo templates API](https://developers.klaviyo.com/en/reference/templates_api_overview)
- [Shopify notification customization](https://help.shopify.com/en/manual/fulfillment/setup/notifications/customizing-notifications)

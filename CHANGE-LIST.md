# Site change list

Notes from the `#coast-charging-co` feedback. Use this as a later punch list. Do not treat it as a request to change everything at once.

The palm silhouette swap is already live and is not part of this list.

## Keep as-is

- The main headline
- The coastal color system
- “Better rides are better together”
- Real local photography
- The simple rider-oriented explanation
- Separate rider and host form destinations
- “Powered by the Coast”
- A relatively short homepage

## Recommended work order

### 1. Fix mobile horizontal overflow

Find and stop whatever still causes sideways scroll on phones (wide decorations, forms, or images).

### 2. Finish About and Roadmap, or hide them

Both pages currently say “under construction.” Either fill them or take them out of the nav until they are ready.

**About page**

- Photo of Kaleb and Steven
- Names and roles
- Why you started Coast
- North County connection
- One real prototype photo
- Current stage: developing and testing the first station
- Contact information

**Roadmap page** — use Now / Next / Later, not dates

- **Now:** building the first direct-DC charging system; validating charging profiles and protection behavior; talking with riders and potential pilot hosts
- **Next:** complete controlled charging tests; finish compact electronics; select the first supervised pilot site
- **Later:** measure rider use and host experience; improve the station from pilot evidence

### 3. Soften unsupported claims

On the homepage:

- Change “It's easy and safe to charge!”
- Change “come back to a full battery!”

Those over-promise for a pre-pilot product.

### 4. Rider signup (local riders, not a generic subscribe)

- Promise: “Follow the build and hear when the first Coast Charger is ready for pilot testing.”
- Button: **Get Coast updates** (hero form and any other Subscribe button — not a generic Subscribe)
- Under the form: “Occasional build updates, local test invitations, and pilot-location news. No weekly spam.”
- Optional field after email: **Where do you usually ride?**

### 5. Add “Built here. Tested here.” before the host section

A compact proof block between the lifestyle content and “Become a Coast Charger Host”:

- Founder photo
- Prototype photo
- North County
- One sentence on direct-DC, solar / off-grid architecture
- Current-stage label
- Link to the roadmap

Example copy:

> We're Kaleb and Steven. We're developing Coast Charging in North County San Diego and currently testing the first direct-DC prototype before selecting a supervised pilot site.

### 6. Replace the host email box with a real inquiry form

A generic subscribe is too weak for prospective hosts (site fit, responsibility, safety, rider demand, appearance, maintenance, pilot scope).

- Heading: **Help bring the first Coast Charger to North County.**
- Body: looking for local businesses and community locations interested in exploring a supervised pilot; tell us about your site and we’ll start with a conversation
- Button: **Discuss a pilot site**
- Fields: name, work email, business or organization, location, type of site

### 7. Welcome emails (MailerLite)

The form is not the end of the funnel. It is the handoff into a relationship.

**Rider welcome — send immediately**

1. Thank them by name if available
2. Explain the current prototype stage
3. Include one real photo
4. Ask what e-bike they ride
5. Ask where they would use a charger
6. Tell them what future emails will contain

**Host welcome — send immediately**

1. Confirm the inquiry reached the team
2. Explain that Coast is in a pre-pilot stage
3. List the information needed about the location
4. Invite a reply or a short conversation
5. Set an expected response time

Without this follow-up, the site collects addresses but does not move people toward research participation, pilot testing, or hosting.

### 8. Conversion events

Vercel Analytics is already installed. Custom conversion events have not been verified. Track these separately:

- `rider_signup_started`
- `rider_signup_completed`
- `host_form_started`
- `host_form_completed`
- `about_viewed`
- `roadmap_viewed`
- `email_clicked`

Useful funnel metrics:

1. Homepage visitor to rider signup
2. Homepage visitor to host inquiry
3. Host-section view to host-form completion
4. Welcome-email response rate
5. Percentage of rider signups who provide bike model and riding area
6. Number of qualified North County host conversations

Raw traffic is secondary at this stage. Some of those metrics live in MailerLite / inbox, not only on the site.

### 9. Search, sharing, and privacy

The live homepage is missing a meta description, canonical URL, Open Graph tags, and a visible robots directive.

Add:

- Title: `Coast Charging Co | E-bike charging in North County San Diego`
- Description: Coast Charging is developing solar-powered e-bike charging stations in North County San Diego. Follow the build or explore hosting a pilot.
- Canonical: `https://coastchargingco.com/`
- `og:title`: Coast Charging Co
- `og:description`: More range for the ride ahead. Built in North County San Diego.
- `og:url`: `https://coastchargingco.com/`
- `og:image`: a real Coast photo
- `og:type`: website

Also add a brief privacy statement near the forms and a privacy page, since the site collects email addresses.

## Need before some of this can ship

- Founder photo and prototype photo
- Roles, and a sentence on why you started Coast (if you want that in your words)
- MailerLite access, or confirmation that fields and the two welcome automations can be added
- A real photo for social sharing (`og:image`)
- Preferred contact email and host response-time wording

## Not verified in the original feedback

- Actual MailerLite confirmation or welcome-email behavior
- Existing conversion rates
- Performance on physical iPhones
- Whether signup events are already tracked in MailerLite
- Whether a privacy policy already exists at an unlinked URL

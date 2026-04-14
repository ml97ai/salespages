#!/usr/bin/env python3
"""Generate legal PDFs for Charts Paradise LLC / Cryptic Hustle."""

from fpdf import FPDF
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

COMPANY = "Charts Paradise LLC"
BRAND = "Cryptic Hustle"
ADDRESS = "30 N Gould St Ste R, Sheridan, Wyoming 82801, United States"
EMAIL = "support@email.90mtrader.com"
DATE = "April 14, 2026"


class LegalPDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(100, 100, 100)
        self.cell(0, 8, f"{COMPANY}  |  {BRAND}", align="C")
        self.ln(5)
        self.set_draw_color(200, 200, 200)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(6)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "", 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}  |  {EMAIL}", align="C")

    def doc_title(self, title):
        self.set_font("Helvetica", "B", 20)
        self.set_text_color(30, 30, 30)
        self.cell(0, 14, title, align="C")
        self.ln(10)
        self.set_font("Helvetica", "", 9)
        self.set_text_color(120, 120, 120)
        self.cell(0, 6, f"Last updated: {DATE}", align="C")
        self.ln(4)
        self.cell(0, 6, f"{COMPANY}  |  {ADDRESS}", align="C")
        self.ln(4)
        self.cell(0, 6, f"Contact: {EMAIL}", align="C")
        self.ln(12)

    def section_heading(self, text):
        self.ln(4)
        self.set_font("Helvetica", "B", 13)
        self.set_text_color(30, 30, 30)
        self.cell(0, 9, text)
        self.ln(7)

    def body_text(self, text):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(50, 50, 50)
        self.multi_cell(0, 5.5, text)
        self.ln(2)

    def bullet_list(self, items):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(50, 50, 50)
        for item in items:
            self.cell(6)
            self.cell(5, 5.5, "-")
            self.multi_cell(0, 5.5, item)
            self.ln(1)
        self.ln(2)

    def numbered_list(self, items):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(50, 50, 50)
        for i, item in enumerate(items, 1):
            self.cell(6)
            self.cell(8, 5.5, f"{i}.")
            self.multi_cell(0, 5.5, item)
            self.ln(1)
        self.ln(2)


# ── TERMS OF SERVICE ──────────────────────────────────────────────

def generate_terms():
    pdf = LegalPDF()
    pdf.alias_nb_pages()
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.add_page()
    pdf.doc_title("Terms of Service")

    pdf.section_heading("1. Agreement to Terms")
    pdf.body_text(f'By accessing or purchasing any product or service from {COMPANY} ("Company," "we," "us," or "our"), operating under the brand name {BRAND}, you ("User," "you," or "your") agree to be bound by these Terms of Service. If you do not agree to these terms, do not use our website or purchase our products.')

    pdf.section_heading("2. Company Information")
    pdf.body_text(f"Legal Entity: {COMPANY}\nAddress: {ADDRESS}\nEmail: {EMAIL}\nBrand: {BRAND}")

    pdf.section_heading("3. Products and Services")
    pdf.body_text("We offer digital educational products related to trading, including but not limited to:")
    pdf.bullet_list([
        "The Precision Trader System (including the Precision Trader Certification course, rPilot software platform, AI trading coach, risk management tools, pass planner, payout planner, and community access)",
        "The 90-Minute Method course",
        "Other digital training products as offered on our website",
    ])
    pdf.body_text("All products are delivered digitally and made available for instant access upon completed payment.")

    pdf.section_heading("4. Account Registration")
    pdf.body_text("To access our products, you may be required to create an account. You are responsible for maintaining the confidentiality of your login credentials and for all activity under your account. You agree to provide accurate, current, and complete information during registration and to keep your account information updated.")

    pdf.section_heading("5. Payment Terms")
    pdf.body_text("Prices for our products are listed on the applicable sales page at the time of purchase. We currently offer the following payment options for The Precision Trader System:")
    pdf.bullet_list([
        "One-time payment: $697 USD",
        "Payment plan: 3 payments of $249 USD",
    ])
    pdf.body_text("All payments are processed through our third-party payment processor. By providing payment information, you represent that you are authorized to use the payment method and authorise us to charge the applicable fees. If you select a payment plan, you authorise recurring charges until the full amount is paid. Failure to complete payment plan instalments may result in suspension of access until all payments are received.")

    pdf.section_heading("6. Lifetime Access")
    pdf.body_text('"Lifetime access" means for the operational life of the product and platform. We reserve the right to discontinue or materially alter the platform with reasonable notice. In the event of discontinuation, we will make reasonable efforts to provide access to course materials in an alternative format.')

    pdf.section_heading("7. Intellectual Property")
    pdf.body_text(f"All content, materials, software, trademarks, and intellectual property provided through our products and services are owned by {COMPANY} or our licensors. Your purchase grants you a personal, non-exclusive, non-transferable licence to access and use the materials for your own personal, non-commercial use.")
    pdf.body_text("You may not:")
    pdf.bullet_list([
        "Copy, reproduce, distribute, or share course materials with any third party",
        "Resell, sublicence, or commercially exploit any content",
        "Record, screenshot, or capture video or audio content for redistribution",
        "Reverse engineer, decompile, or attempt to extract source code from the rPilot software",
        "Use our trademarks, logos, or branding without written permission",
    ])
    pdf.body_text("Violation of these terms may result in immediate termination of access without refund.")

    pdf.section_heading("8. Community Guidelines")
    pdf.body_text("Access to the Discord community and accountability pods is subject to our community guidelines. We reserve the right to remove any user who engages in harassment, spam, hate speech, sharing of copyrighted materials, promotion of competing products, or any behaviour that disrupts the community experience. Removal from the community for violation of guidelines does not entitle you to a refund.")

    pdf.section_heading("9. User Conduct")
    pdf.body_text("You agree not to:")
    pdf.bullet_list([
        "Use our products for any unlawful purpose",
        "Share your account credentials with others",
        "Attempt to gain unauthorized access to our systems or other users' accounts",
        "Interfere with or disrupt the operation of our platform",
        "Use automated means to access or scrape our content",
    ])

    pdf.section_heading("10. Limitation of Liability")
    pdf.body_text(f"To the maximum extent permitted by law, {COMPANY}, its owners, officers, employees, and affiliates shall not be liable for any indirect, incidental, special, consequential, or punitive damages, including but not limited to loss of profits, trading losses, data loss, or other intangible losses, resulting from:")
    pdf.bullet_list([
        "Your use of or inability to use our products or services",
        "Any trading decisions you make based on our educational content",
        "Unauthorized access to your account",
        "Any interruption or cessation of our services",
        "Any errors or omissions in our content",
    ])
    pdf.body_text("Our total liability for any claim arising from these terms or your use of our products shall not exceed the amount you paid for the product giving rise to the claim.")

    pdf.section_heading("11. Indemnification")
    pdf.body_text(f"You agree to indemnify and hold harmless {COMPANY}, its owners, officers, employees, and affiliates from any claims, damages, losses, liabilities, costs, or expenses (including legal fees) arising from your use of our products, violation of these terms, or infringement of any third-party rights.")

    pdf.section_heading("12. Governing Law")
    pdf.body_text("These Terms of Service are governed by and construed in accordance with the laws of the State of Wyoming, United States, without regard to conflict of law principles. Any disputes arising from these terms shall be resolved in the courts of Sheridan County, Wyoming.")

    pdf.section_heading("13. Changes to Terms")
    pdf.body_text('We reserve the right to modify these terms at any time. Changes will be posted on this page with an updated "Last updated" date. Your continued use of our products after changes are posted constitutes acceptance of the revised terms.')

    pdf.section_heading("14. Severability")
    pdf.body_text("If any provision of these terms is found to be unenforceable or invalid, that provision will be limited or eliminated to the minimum extent necessary, and the remaining provisions will remain in full force and effect.")

    pdf.section_heading("15. Contact")
    pdf.body_text(f"For questions about these Terms of Service, contact us at {EMAIL}.")

    pdf.output(os.path.join(OUTPUT_DIR, "Terms-of-Service.pdf"))
    print("Created Terms-of-Service.pdf")


# ── PRIVACY POLICY ────────────────────────────────────────────────

def generate_privacy():
    pdf = LegalPDF()
    pdf.alias_nb_pages()
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.add_page()
    pdf.doc_title("Privacy Policy")

    pdf.section_heading("1. Introduction")
    pdf.body_text(f'{COMPANY} ("we," "us," or "our"), operating under the brand name {BRAND}, is committed to protecting your privacy. This Privacy Policy explains how we collect, use, disclose, and safeguard your personal information when you visit our website, purchase our products, or use our services.')

    pdf.section_heading("2. Information We Collect")
    pdf.body_text("Information you provide directly:")
    pdf.bullet_list([
        "Account information: name, email address, and password when you create an account",
        "Payment information: billing address and payment details (processed securely by our third-party payment processor; we do not store full credit card numbers)",
        "Communication data: any information you provide when contacting our support team",
        "Community content: messages, posts, and other content you share in our Discord community",
        "Trading data: trade logs and performance data you voluntarily enter into the rPilot platform (this data is used solely to provide you with personalized analytics and coaching)",
    ])
    pdf.body_text("Information collected automatically:")
    pdf.bullet_list([
        "Device and browser information: IP address, browser type, operating system, device type",
        "Usage data: pages visited, time spent on pages, click patterns, referring URLs",
        "Cookies and tracking technologies: as described in our Cookie Policy",
    ])

    pdf.section_heading("3. How We Use Your Information")
    pdf.body_text("We use your information to:")
    pdf.bullet_list([
        "Process purchases and deliver digital products",
        "Provide access to the rPilot platform and generate personalized trading analytics",
        "Provide the AI coaching features within rPilot",
        "Send transactional emails (purchase confirmations, account updates, product access)",
        "Send marketing emails (product updates, promotions, educational content) where you have opted in or where we have a legitimate interest",
        "Provide customer support",
        "Improve our products, services, and website",
        "Analyse usage patterns to enhance user experience",
        "Prevent fraud and protect the security of our platform",
        "Comply with legal obligations",
    ])

    pdf.section_heading("4. Legal Basis for Processing (GDPR)")
    pdf.body_text("If you are located in the European Economic Area (EEA) or United Kingdom, we process your personal data on the following legal bases:")
    pdf.bullet_list([
        "Contract performance: to deliver the products and services you purchased",
        "Legitimate interest: to improve our services, prevent fraud, and send relevant marketing communications",
        "Consent: where you have explicitly consented to specific processing activities (e.g., marketing emails)",
        "Legal obligation: to comply with applicable laws and regulations",
    ])

    pdf.section_heading("5. Data Sharing and Third Parties")
    pdf.body_text("We do not sell your personal information. We may share your data with:")
    pdf.bullet_list([
        "Payment processors: to process transactions securely",
        "Email service providers: to send transactional and marketing emails",
        "Hosting providers: to host our website and platform",
        "Analytics providers: to understand website usage (in anonymized or aggregated form where possible)",
        "Discord: our community platform (subject to Discord's own privacy policy)",
        "Legal authorities: when required by law, subpoena, or court order",
    ])
    pdf.body_text("All third-party service providers are contractually bound to handle your data securely and only for the purposes we specify.")

    pdf.section_heading("6. Data Retention")
    pdf.body_text("We retain your personal data for as long as your account is active or as needed to provide our services. If you request account deletion, we will delete or anonymise your data within 30 days, except where we are required to retain it for legal, accounting, or regulatory purposes.")
    pdf.body_text("Trading data you enter into rPilot is retained for as long as your account is active. You may export or delete your trading data at any time through the platform.")

    pdf.section_heading("7. Your Rights")
    pdf.body_text("Depending on your location, you may have the following rights:")
    pdf.bullet_list([
        "Access: request a copy of the personal data we hold about you",
        "Rectification: request correction of inaccurate data",
        "Erasure: request deletion of your personal data",
        "Restriction: request restriction of processing",
        "Portability: request your data in a portable format",
        "Objection: object to processing based on legitimate interest",
        "Withdraw consent: where processing is based on consent, withdraw at any time",
        "Unsubscribe: opt out of marketing emails at any time via the unsubscribe link in any email",
    ])
    pdf.body_text(f"To exercise any of these rights, contact us at {EMAIL}. We will respond within 30 days.")

    pdf.section_heading("8. Data Security")
    pdf.body_text("We implement appropriate technical and organizational measures to protect your personal data, including 256-bit SSL encryption for data in transit, secure servers, and access controls. However, no method of electronic transmission or storage is 100% secure, and we cannot guarantee absolute security.")

    pdf.section_heading("9. International Transfers")
    pdf.body_text("Your data may be transferred to and processed in the United States and other countries where our service providers operate. If you are located in the EEA or UK, we ensure appropriate safeguards are in place for such transfers, including standard contractual clauses approved by the European Commission.")

    pdf.section_heading("10. Children's Privacy")
    pdf.body_text("Our products and services are not intended for individuals under the age of 18. We do not knowingly collect personal information from children. If we learn that we have collected data from a child under 18, we will delete it promptly.")

    pdf.section_heading("11. California Residents (CCPA)")
    pdf.body_text("If you are a California resident, you have additional rights under the California Consumer Privacy Act (CCPA):")
    pdf.bullet_list([
        "The right to know what personal information we collect, use, and disclose",
        "The right to request deletion of your personal information",
        "The right to opt out of the sale of personal information (we do not sell your data)",
        "The right to non-discrimination for exercising your privacy rights",
    ])
    pdf.body_text(f"To exercise these rights, contact us at {EMAIL}.")

    pdf.section_heading("12. Changes to This Policy")
    pdf.body_text("We may update this Privacy Policy from time to time. Changes will be posted on this page with an updated date. We encourage you to review this page periodically.")

    pdf.section_heading("13. Contact")
    pdf.body_text(f"For privacy-related questions or requests, contact us at {EMAIL}.")

    pdf.output(os.path.join(OUTPUT_DIR, "Privacy-Policy.pdf"))
    print("Created Privacy-Policy.pdf")


# ── REFUND POLICY ─────────────────────────────────────────────────

def generate_refund():
    pdf = LegalPDF()
    pdf.alias_nb_pages()
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.add_page()
    pdf.doc_title("Refund Policy")

    pdf.section_heading("1. The 30-Day Precision Guarantee")
    pdf.body_text(f"We offer a 30-day money-back guarantee on The Precision Trader System. We stand behind our product and believe that anyone who genuinely uses the system will see results. To ensure every refund request comes from someone who has given the system a real chance, we ask that you complete the steps below before requesting a refund.")

    pdf.section_heading("2. Eligibility Requirements")
    pdf.body_text("To qualify for a full refund, all of the following must be completed within 30 days of your purchase date:")
    pdf.numbered_list([
        "Complete the training: Watch all 6 modules of the Precision Trader Certification in full. Your account activity will show module completion status.",
        "Log at least 20 trades in rPilot: Each trade must include the required fields (entry, exit, risk amount, and a brief trade note). rPilot begins generating personalized insights after 20 logged trades - this is the minimum needed to experience the system working for you.",
        "Use the Risk Shield tool: Apply the recommended risk amount from Risk Shield on at least 10 of your logged trades. This ensures you've followed the personalized risk guidance rather than guessing.",
        "Submit your refund request within 30 days of your original purchase date.",
    ])
    pdf.body_text("These requirements exist because the system is built to work when you use it. We want to make sure you've experienced the full value before making your decision.")

    pdf.section_heading("3. How to Request a Refund")
    pdf.body_text(f"To request a refund, email us at {EMAIL} with the following:")
    pdf.bullet_list([
        "Your full name",
        "The email address used for purchase",
        "Your date of purchase",
        "A screenshot of your rPilot dashboard showing your logged trades (minimum 20)",
        "Confirmation that you have completed all 6 course modules",
    ])
    pdf.body_text("Our team will verify completion of the eligibility steps above using your account data. Once verified, your refund will be processed - no questions asked about why you want one.")

    pdf.section_heading("4. Refund Processing")
    pdf.body_text("Once your refund request is verified, we will process your refund within 5-10 business days. The refund will be issued to the original payment method used at checkout. Depending on your bank or credit card provider, it may take an additional 5-10 business days for the refund to appear on your statement.")

    pdf.section_heading("5. Payment Plans")
    pdf.body_text("If you purchased via the 3-payment plan ($249 x 3) and request a refund within 30 days:")
    pdf.bullet_list([
        "We will refund all payments made to date",
        "Any remaining scheduled payments will be cancelled",
    ])

    pdf.section_heading("6. Post-Refund Access")
    pdf.body_text("Upon processing a refund, your access to The Precision Trader System will be revoked, including:")
    pdf.bullet_list([
        "Course materials and video content",
        "rPilot platform access",
        "Community and Discord access",
        "AI coaching features",
    ])
    pdf.body_text("You may export your trading data from rPilot before your refund is processed.")

    pdf.section_heading("7. Exceptions")
    pdf.body_text("Refunds are not available in the following circumstances:")
    pdf.bullet_list([
        "Requests made after the 30-day guarantee period has expired",
        "Eligibility requirements (Section 2) have not been completed",
        "Accounts terminated for violation of our Terms of Service or Community Guidelines",
        "Chargebacks or payment disputes filed without first contacting us directly",
    ])
    pdf.body_text("We encourage you to contact us directly before initiating a dispute with your payment provider. We are committed to resolving issues quickly and fairly.")

    pdf.section_heading("8. Digital Product Acknowledgement")
    pdf.body_text("By purchasing our products, you acknowledge that you are purchasing a digital product with instant access. Under EU consumer law, you have the right to withdraw from a purchase within 14 days. However, by accessing the digital content immediately upon purchase, you acknowledge that you waive the 14-day withdrawal right for digital content that has been fully provided, in accordance with the Consumer Rights Directive (2011/83/EU). Our 30-day guarantee exceeds this statutory requirement and serves as your primary protection.")

    pdf.section_heading("9. Contact")
    pdf.body_text(f"For refund requests or questions, contact us at {EMAIL}.")

    pdf.output(os.path.join(OUTPUT_DIR, "Refund-Policy.pdf"))
    print("Created Refund-Policy.pdf")


if __name__ == "__main__":
    generate_terms()
    generate_privacy()
    generate_refund()
    print("\nAll PDFs generated successfully.")

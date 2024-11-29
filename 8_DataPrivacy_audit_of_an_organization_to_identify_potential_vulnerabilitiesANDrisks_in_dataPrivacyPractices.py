import datetime

class DataPrivacyAudit:
    def __init__(self, organization_name):
        self.organization_name = organization_name
        self.audit_date = datetime.datetime.now().strftime("%Y-%m-%d")
        self.responses = {}

    def ask_question(self, category, question):
        print(f"\n{category} - {question}")
        response = input("Enter your response (Yes/No/Partial/NA): ").strip().lower()
        comments = input("Additional comments (optional): ")
        self.responses[question] = {"response": response, "comments": comments}

    def conduct_audit(self):
        print(f"\nStarting Data Privacy Audit for {self.organization_name}")
        print(f"Audit Date: {self.audit_date}")

        # 1. Data Collection Practices
        self.ask_question("Data Collection", "Does the organization collect only necessary data?")
        self.ask_question("Data Collection", "Are individuals informed about the data being collected?")
        self.ask_question("Data Collection", "Is sensitive data handled with extra protection measures?")

        # 2. Data Storage and Security
        self.ask_question("Data Storage", "Is personal data stored securely with encryption?")
        self.ask_question("Data Storage", "Are access controls in place to limit data access to authorized personnel?")
        self.ask_question("Data Storage", "Are data retention policies clearly defined and followed?")

        # 3. Data Usage and Sharing
        self.ask_question("Data Usage", "Is data usage limited to the stated purposes in the privacy policy?")
        self.ask_question("Data Usage", "Is personal data shared only with consent or legitimate reason?")

        # 4. Data Subject Rights
        self.ask_question("Data Subject Rights", "Does the organization have a process for data access requests?")
        self.ask_question("Data Subject Rights", "Is there a mechanism to update or delete personal data upon request?")

        # 5. Incident Response and Breach Notification
        self.ask_question("Incident Response", "Is there a protocol in place for data breach response?")
        self.ask_question("Incident Response", "Are affected individuals notified promptly in case of a data breach?")

        # 6. Third-Party Management
        self.ask_question("Third-Party Management", "Are third-party data processors vetted for data privacy compliance?")
        self.ask_question("Third-Party Management", "Are data-sharing agreements in place with all vendors handling personal data?")

        # 7. Employee Training and Awareness
        self.ask_question("Employee Training", "Do employees receive regular data privacy and security training?")
        self.ask_question("Employee Training", "Are employees educated on data privacy laws and best practices?")

        print("\nAudit Complete. Generating Report...")

    def generate_report(self):
        print(f"\nData Privacy Audit Report for {self.organization_name}")
        print(f"Audit Date: {self.audit_date}\n")

        for question, response in self.responses.items():
            print(f"Question: {question}")
            print(f"Response: {response['response'].capitalize()}")
            if response["comments"]:
                print(f"Comments: {response['comments']}")
            print("\n" + "-" * 50)

# Example Usage
organization_name = input("Enter the organization's name for the audit: ")
audit = DataPrivacyAudit(organization_name)
audit.conduct_audit()
audit.generate_report()

import datetime

class DataProtectionCompliancePlan:
    def __init__(self, organization_name):
        self.organization_name = organization_name
        self.assessment_date = datetime.datetime.now().strftime("%Y-%m-%d")
        self.compliance_plan = {}

    def add_requirement(self, requirement, description):
        print(f"\nRequirement: {requirement}")
        print(f"Description: {description}")
        status = input("Is this requirement currently being met? (Yes/No/Partial): ").strip().lower()
        
        if status in ("no", "partial"):
            action_items = input("Enter actions needed to ensure compliance (e.g., update policy, implement training): ").strip()
        else:
            action_items = "No additional actions needed"

        self.compliance_plan[requirement] = {
            "status": status.capitalize(),
            "action_items": action_items
        }

    def conduct_assessment(self):
        print(f"\nStarting Compliance Assessment for {self.organization_name} on {self.assessment_date}\n")

        # List of common data protection requirements
        requirements = [
            ("Data Collection Consent", "Collect and process personal data only with explicit consent."),
            ("Purpose Limitation", "Data should be collected for specified, legitimate purposes only."),
            ("Data Minimization", "Only collect and process data that is strictly necessary."),
            ("Accuracy", "Ensure personal data is accurate and regularly updated."),
            ("Storage Limitation", "Do not store personal data for longer than necessary."),
            ("Data Security", "Protect personal data against unauthorized or unlawful processing, loss, or damage."),
            ("Data Subject Rights", "Provide individuals with rights to access, correct, and delete their data."),
            ("Breach Notification", "Notify authorities and affected individuals in the event of a data breach."),
            ("Third-Party Compliance", "Ensure third-party partners comply with data protection standards."),
            ("Employee Training", "Provide regular training on data privacy and protection policies.")
        ]

        # Iterate through each requirement, gathering responses and actions
        for req, desc in requirements:
            self.add_requirement(req, desc)

        print("\nAssessment Complete. Generating Compliance Plan...\n")

    def generate_compliance_plan(self):
        print(f"\nCompliance Plan for {self.organization_name}")
        print(f"Assessment Date: {self.assessment_date}")
        print("=" * 50)
        for req, details in self.compliance_plan.items():
            print(f"Requirement: {req}")
            print(f"Current Status: {details['status']}")
            print(f"Actions Needed: {details['action_items']}")
            print("-" * 50)

# Example Usage
organization_name = input("Enter the organization's name for the compliance assessment: ")
compliance_assessment = DataProtectionCompliancePlan(organization_name)
compliance_assessment.conduct_assessment()
compliance_assessment.generate_compliance_plan()

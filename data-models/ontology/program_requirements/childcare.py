"""Child Care Assistance requirements."""
from .. import documents
from .. import information

# See forms CFWB-012, 012A, 012B.
# https://www.nyc.gov/assets/acs/pdf/early-care-education/forms/2022/CFWB012.pdf

# See additional forms:
# https://www.nyc.gov/site/acs/early-care/forms.page


childcare_general_info = {
    information.Residence: [
        documents.LocalID,
        documents.DriversLicense,
        documents.UtilityBill,
        documents.RentReceipt,
        documents.Lease,
        documents.Section8AwardLetter,
        documents.PublicHousingCertificate,
        documents.SelfResidenceStatement,
    ],
    information.ParentRelationship: [
        documents.BirthCertificate,
        documents.AdoptionRecord,
        documents.BaptismCertificate,
        documents.Passport,
        documents.FamilyCourtStatement,
    ],
    information.CitizenshipStatus: [
        documents.BirthCertificate,
        documents.HospitalRecord,
        documents.USPassport,
        documents.NaturalizationCertificate,
        documents.FS_240BirthAbroadDocument,
    ],
    information.Age: [
        documents.BirthCertificate,
        documents.AdoptionRecord,
        documents.BaptismCertificate,
        documents.Passport,
        documents.NaturalizationCertificate,
    ],
}

childcare_earned_income_info = {
    information.EmploymentIncome: [
        documents.EmployerStatement,
        documents.EmploymentCheck,
    ],
    information.SelfEmploymentIncome: [
        documents.SelfEmploymentRecord,
        documents.IncomeTaxRecord,
    ],
}

childcare_unearned_income_info = {
    information.SupplementalSecurityIncome: [
        documents.BankStatement,
        documents.SocialSecurityLetter,
        documents.SocialSecurityCheck,
    ],
    information.SocialSecurityDisabilityIncome: [
        documents.BankStatement,
        documents.SocialSecurityLetter,
        documents.SocialSecurityCheck,
    ],
    information.SocialSecurityDependentBenefits: [
        documents.BankStatement,
        documents.SocialSecurityLetter,
        documents.SocialSecurityCheck,
    ],
    information.SocialSecuritySurvivorsBenefits: [
        documents.BankStatement,
        documents.SocialSecurityLetter,
        documents.SocialSecurityCheck,
    ],
    information.SocialSecurityRetirementBenefits: [
        documents.BankStatement,
        documents.SocialSecurityLetter,
        documents.SocialSecurityCheck,
    ],
    information.RailroadRetirementIncome: [
        documents.BankStatement,
        documents.RetirementRecord,
    ],
    information.PensionIncome: [
        documents.PensionStatement,
        documents.BankStatement,
        documents.RetirementRecord,
    ],
    information.InterestDividendRoyaltyIncome: [
        documents.BankStatement,
    ],
    information.WorkersCompensation: [
        documents.BankStatement,
    ],
    information.UnemploymentInsuranceIncome: [
        documents.BankStatement,
        documents.UnemploymentInsuranceCheck,
        documents.UnemploymentInsuranceLetter,
    ],
    information.DisabilityIncome: [
        documents.BankStatement,
        documents.StateDisabilityCheck,
        documents.StateDisabilityLetter,
    ],
    information.VeteransIncome: [
        documents.BankStatement,
        documents.VeteransAffairsLetter,
    ],
    information.PublicAssistanceGrant: [
        documents.BankStatement,
    ],
    information.GIDependencyAllotment: [
        documents.BankStatement,
        documents.VeteransAffairsLetter,
    ],
    information.EducationGrantIncome: [
        documents.BankStatement,
    ],
    information.EducationLoanIncome: [
        documents.BankStatement,
    ],
    information.GiftIncome: [
        documents.BankStatement,
    ],
    information.FosterCareIncome: [
        documents.BankStatement,
    ],
    information.ChildSupportIncome: [
        documents.BankStatement,
    ],
    information.SpousalSupportIncome: [
        documents.BankStatement,
    ],
    information.PrivateDisabilityInsuranceIncome: [
        documents.BankStatement,
    ],
    information.NoFaultInsuranceIncome: [
        documents.BankStatement,
    ],
    information.UnionBenefitIncome: [
        documents.BankStatement,
    ],
    information.LoanIncome: [
        documents.BankStatement,
    ],
    information.TrustIncome: [
        documents.BankStatement,
    ],
    information.TrainingStipendIncome: [
        documents.BankStatement,
    ],
    information.BoarderLodgerIncome: [
        documents.BankStatement,
        documents.RentalIncomeStatement,
        documents.RentalIncomeCheck,
    ],
    information.RentIncome: [
        documents.RentalIncomeCheck,
        documents.RentalIncomeStatement,
    ],
}

childcare_rationale_info = {
    information.HoursWorked: [
        documents.EmployerStatement,
    ],
    information.EducationStatus: [
        documents.SchoolEnrollmentRecord,
        documents.SchoolAttendanceRecord,
    ],
    information.SeekingEmployment: [
        documents.WorkSearchRecord,
        documents.UnemploymentInsuranceCheck,
        documents.UnemploymentInsuranceLetter,
    ],
    information.IsHomeless: [
        documents.HomelessShelterStatement,
        documents.SelfResidenceStatement,
    ],
    information.DomesticViolenceSupport: [
        documents.CommunityOrganizationStatement,
    ],
}

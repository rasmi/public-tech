"""SNAP requirements."""
from .. import documents
from .. import information

# See forms LDSS-4826 and LDSS-4826A:
# https://otda.ny.gov/programs/applications/4826.pdf
# https://otda.ny.gov/programs/applications/4826A.pdf

# See form LDSS-2921 and PUB-1301:
# https://otda.ny.gov/programs/applications/2921.pdf
# https://otda.ny.gov/programs/applications/1301.pdf

# See Form W-129G:
# https://www.nyc.gov/assets/hra/downloads/pdf/services/snap/eligibility_factors_and_suggested_documentation_guide.pdf

# See additional forms:
# https://otda.ny.gov/programs/applications/


snap_general_info = {
    information.IdentityInformation: [
        documents.StateID,
        documents.DriversLicense,
        documents.MilitaryID,
        documents.USPassport,
        documents.NaturalizationCertificate,
        documents.HospitalRecord,
        documents.AdoptionRecord,
        documents.BirthCertificate,
        documents.BaptismCertificate,
        documents.VoterRegistrationCard,
    ],
    information.Age: [
        documents.StateID,
        documents.DriversLicense,
        documents.USPassport,
        documents.NaturalizationCertificate,
        documents.HospitalRecord,
        documents.AdoptionRecord,
        documents.BirthCertificate,
        documents.BaptismCertificate,
    ],
    information.SocialSecurityNumber: [
        documents.SocialSecurityCard,
        documents.SocialSecurityLetter,
    ],
    information.Residence: [
        documents.Lease,
        documents.RentReceipt,
        documents.LandlordStatement,
        documents.MortgageRecord,
        documents.SchoolRecord,
    ],
    information.HouseholdComposition: [
        documents.LandlordStatement,
        documents.PersonStatement,
        documents.CommunityOrganizationStatement,
    ],
    information.CitizenshipStatus: [
        documents.BirthCertificate,
        documents.HospitalRecord,
        documents.USPassport,
        documents.MilitaryRecord,
        documents.NaturalizationCertificate,
    ],
    information.ImmigrationStatus: [
        documents.PermanentResidentCard,
        documents.VisaDocument,
        documents.I_94ArrivalDepartureRecord,
        documents.I_7668EmploymentAuthorizationDocument,
        documents.I_668BEmploymentAuthorizationDocument,
        documents.ResidenceHistoryRecord,
    ],
}

snap_earned_income_info = {
    information.HoursWorked: [
        documents.EmployerStatement,
    ],
    information.EmploymentIncome: [
        documents.EmployerStatement,
        documents.EmploymentCheck,
        documents.IncomeTaxReturn,
        documents.SelfEmploymentRecord,
    ],
    information.RentIncome: [
        documents.RentalIncomeCheck,
        documents.RentalIncomeStatement,
    ],
}

snap_unearned_income_info = {
    information.SupplementalSecurityIncome: [],  # No verification necessary for SSI in NYC.
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
}

snap_resource_info = {
    information.CashResource: [],
    information.CheckingAccountBalance: [
        documents.BankStatement,
    ],
    information.SavingsAccountBalance: [
        documents.BankStatement,
    ],
    information.CreditUnionAccountBalance: [
        documents.BankStatement,
    ],
    information.StockResourceInformation: [
        documents.BankStatement,
        documents.BrokerageStatement,
    ],
    information.BondResourceInformation: [
        documents.BankStatement,
        documents.BrokerageStatement,
    ],
    information.LifeInsuranceResource: [
        documents.LifeInsurancePolicy,
    ],
    information.SavingsBondResource: [
        documents.BankStatement,
        documents.BrokerageStatement,
    ],
    information.TrustFundInformation: [
        documents.BankStatement,
        documents.BrokerageStatement,
    ],
    information.VehicleResource: [
        documents.VehicleRegistration,
        documents.VehicleTitle,
    ],
    information.OwnedHomeInformation: [
        documents.MortgageRecord,
        documents.PropertyDeed,
    ],
    information.HealthInsuranceInformation: [
        documents.HealthInsurancePolicy,
        documents.MedicareLetter,
    ],
}

snap_expense_info = {
    information.RentExpense: [
        documents.RentReceipt,
        documents.RentBill,
        documents.Lease,
        documents.LandlordStatement,
    ],
    information.MortgageExpense: [
        documents.MortgageRecord,
    ],
    information.MortgageHomeownersInsuranceExpense: [
        documents.HomeownersInsuranceBill,
    ],
    information.MortgagePropertyTaxExpense: [
        documents.PropertyTaxRecord,
    ],
    information.UtilityExpense: [
        documents.UtilityBill,
    ],
    information.ChildSupportOwed: [
        documents.ChildSupportPayerStatement,
    ],
    information.ChildSupportPaid: [
        documents.ChildSupportPayerStatement,
    ],
    information.ChildCareExpense: [
        documents.ChildCareProviderStatement,
    ],
    information.MedicalExpense: [
        documents.MedicalBill,
        documents.HealthInsuranceBill,
    ],
    information.MedicaidSpendDown: [
        documents.MedicaidLetter,
    ],
    information.TuitionFeesExpense: [
        documents.TuitionBill,
    ],
}

snap_other_info = {
    information.DrugAlcoholTreatmentFacility: [
        documents.PhysicianStatement,
    ],
    information.ServedInMilitary: [
        documents.MilitaryRecord,
        documents.MilitaryID,
        documents.VeteransAffairsLetter,
    ],
    information.PregnancyInformation: [
        documents.PhysicianStatement,
    ],
    information.UnableToWorkFromDisability: [
        documents.PhysicianStatement,
        documents.SocialSecurityLetter,
    ],
}

snap_compliance_info = {
    information.FleeingFelonyLawEnforcement: [],
    information.ViolatingProbationParole: [],
    information.IntentionalProgramViolation: [],
    information.TradingBenefitsForFirearmsDrugs: [],
    information.BuyingSellingSNAPFraud: [],
    information.PublicAssistanceFraudTwoOrMoreStates: [],
    information.TransferredPropertyToGetBenefits: [],
}

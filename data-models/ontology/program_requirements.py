"""Program requirements."""
import documents
import information

# See forms LDSS-4826 and LDSS-4826A:
# https://otda.ny.gov/programs/applications/4826.pdf
# https://otda.ny.gov/programs/applications/4826A.pdf

# See form LDSS-2921 and PUB-1301:
# https://otda.ny.gov/programs/applications/2921.pdf
# https://otda.ny.gov/programs/applications/1301.pdf

# See Form W-129G:
# https://www.nyc.gov/assets/hra/downloads/pdf/services/snap/eligibility_factors_and_suggested_documentation_guide.pdf

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
    information.SupplementalSecurityIncome,
    information.SocialSecurityDisabilityIncome,
    information.SocialSecurityDependentBenefits,
    information.SocialSecuritySurvivorsBenefits,
    information.SocialSecurityRetirementBenefits,
    information.RailroadRetirementIncome,
    information.PensionIncome,
    information.InterestDividendRoyaltyIncome,
    information.WorkersCompensation,
    information.DisabilityIncome,
    information.VeteransIncome,
    information.PublicAssistanceGrant,
    information.GIDependencyAllotment,
    information.EducationGrantIncome,
    information.EducationLoanIncome,
    information.GiftIncome,
    information.FosterCareIncome,
    information.ChildSupportIncome,
    information.SpousalSupportIncome,
    information.PrivateDisabilityInsuranceIncome,
    information.NoFaultInsuranceIncome,
    information.UnionBenefitIncome,
    information.LoanIncome,
    information.TrustIncome,
    information.TrainingStipendIncome,
    information.BoarderLodgerIncome,
}

snap_resource_info = {
    information.CashResource,
    information.CheckingAccountBalance,
    information.SavingsAccountBalance,
    information.CreditUnionAccountBalance,
    information.StockResourceInformation,
    information.BondResourceInformation,
    information.SavingsBondResource,
    information.TrustFundInformation,
    information.VehicleResource,
}

snap_expense_info = {
    information.RentExpense,
    information.MortgageExpense,
    information.MortgageHomeownersInsuranceExpense,
    information.MortgagePropertyTaxExpense,
    information.UtilityExpense,
    information.ChildSupportOwed,
    information.ChildSupportPaid,
    information.MedicalExpense,
    information.MedicaidSpendDown,
    information.TuitionFeesExpense,
}

snap_other_info = {
    information.DrugAlcoholTreatmentFacility,
    information.ServedInMilitary,
    information.PregnancyInformation,
    information.UnableToWorkFromDisability,
    information.TransferredPropertyToGetBenefits,
}

snap_compliance_info = {
    information.FleeingFelonyLawEnforcement,
    information.ViolatingProbationParole,
    information.IntentionalProgramViolation,
    information.TradingBenefitsForFirearmsDrugs,
    information.BuyingSellingSNAPFraud,
    information.PublicAssistanceFraudTwoOrMoreStates,
}

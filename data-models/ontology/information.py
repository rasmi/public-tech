"""Information types."""


class Information:
    pass


class CitizenshipInformation(Information):
    pass


class EmploymentInformation(Information):
    pass


class ExpenseInformation(Information):
    pass


class HealthInformation(Information):
    pass


class HouseholdInformation(Information):
    pass


class IdentityInformation(Information):
    pass


class IncomeInformation(Information):
    pass


class PersonalInformation(Information):
    pass


class RelationshipInformation(Information):
    pass


class ResourceInformation(Information):
    pass


class ShelterInformation(Information):
    pass


# Citizenship information


class CitizenshipStatus(CitizenshipInformation):
    pass


# Employment information


class EmploymentStatus(EmploymentInformation):
    pass


class PreviousEmployment(EmploymentInformation):
    pass


# Expense information


class AlimonyPaid(ExpenseInformation):
    pass


class ArcherMSADeduction(ExpenseInformation):
    pass


class BusinessExpense(ExpenseInformation):
    pass


class DeductibleBusinessExpense(BusinessExpense):
    pass


class CarPaymentExpense(ExpenseInformation):
    pass


class ChildCareExpense(ExpenseInformation):
    pass


class ChildSupportOwed(ExpenseInformation):
    pass


class ChildSupportPaid(ExpenseInformation):
    pass


class CreditCardPaymentExpense(ExpenseInformation):
    pass


class DependentCareExpense(ExpenseInformation):
    pass


class DomesticProductionActivitiesDeduction(ExpenseInformation):
    pass


class EarlyWithdrawalPenaltyDeduction(ExpenseInformation):
    pass


class EducatorExpense(ExpenseInformation):
    pass


class HSADeduction(ExpenseInformation):
    pass


class InsuranceExpense(ExpenseInformation):
    pass


class IRADeduction(ExpenseInformation):
    pass


class JobRelatedMovingExpense(ExpenseInformation):
    pass


class LoanPaymentExpense(ExpenseInformation):
    pass


class MedicalExpense(ExpenseInformation):
    pass


class SelfEmployedRetirementDeduction(ExpenseInformation):
    pass


class SelfEmploymentHealthInsuranceDeduction(ExpenseInformation):
    pass


class SelfEmploymentTaxDeduction(ExpenseInformation):
    pass


class ShelterExpense(ExpenseInformation, ShelterInformation):
    pass


class MortgageExpense(ShelterExpense):
    pass


class MortgageAssessmentExpense(MortgageExpense):
    pass


class MortgageHomeownersInsuranceExpense(MortgageExpense):
    pass


class MortgageInterestExpense(MortgageExpense):
    pass


class MortgagePrincipalExpense(MortgageExpense):
    pass


class MortgageTaxExpense(MortgageExpense):
    pass


class MortgageEscrowTaxExpense(MortgageTaxExpense):
    pass


class MortgagePropertyTaxExpense(MortgageTaxExpense):
    pass


class RentExpense(ShelterExpense):
    pass


class RoomAndBoardExpense(ShelterExpense):
    pass


class TrailerLotExpense(ShelterExpense):
    pass


class SIMPLEDeduction(ExpenseInformation):
    pass


class SpousalSupportPaid(ExpenseInformation):
    pass


class StudentLoanInterestDeduction(ExpenseInformation):
    pass


class TuitionFeesExpense(ExpenseInformation):
    pass


class UnpaidBillInformation(ExpenseInformation):
    pass


class UtilityExpense(ExpenseInformation):
    pass


class AirConditioningExpense(UtilityExpense):
    pass


class ElectricityExpense(UtilityExpense):
    pass


class NaturalGasExpense(UtilityExpense):
    pass


class PropaneExpense(UtilityExpense):
    pass


class SewerExpense(UtilityExpense):
    pass


class TrashExpense(UtilityExpense):
    pass


class WaterUtilityExpense(UtilityExpense):
    pass


# Health information


class HealthFinanceInformation(HealthInformation):
    pass


class HealthInsuranceInformation(HealthFinanceInformation):
    pass


class AccidentInsuranceInformation(HealthInsuranceInformation):
    pass


class MedicaidSpendDown(HealthInsuranceInformation):
    pass


class MedicareInformation(HealthInsuranceInformation):
    pass


class WillBillingInsuranceCauseHarm(HealthInsuranceInformation):
    pass


class NonMedicareGovernmentBillPayment(HealthFinanceInformation):
    pass


class RecentMedicalBills(HealthFinanceInformation):
    pass


class MedicalInformation(HealthInformation):
    pass


class AccidentInformation(MedicalInformation):
    pass


class RecentCarAccident(AccidentInformation):
    pass


class RecentWorkAccident(AccidentInformation):
    pass


class DisabilityInformation(MedicalInformation):
    pass


class Blindness(DisabilityInformation):
    pass


class DailyLimitedActivityFromDisability(DisabilityInformation):
    pass


class DevelopmentalDisability(DisabilityInformation):
    pass


class UnableToWorkFromDisability(DisabilityInformation):
    pass


class DrugOrAlcoholDependent(MedicalInformation):
    pass


class InMedicalInstitution(MedicalInformation):
    pass


class InHospital(InMedicalInstitution):
    pass


class InNursingHome(InMedicalInstitution):
    pass


class PregnancyInformation(MedicalInformation):
    pass


class TreatmentInformation(MedicalInformation):
    pass


class DrugOrAlcoholTreatment(TreatmentInformation):
    pass


class PersonalCareInformation(HealthInformation):
    pass


class HealthAideInformation(PersonalCareInformation):
    pass


class NeedsHomeOrPersonalCare(PersonalCareInformation):
    pass


# Household information


class HouseholdComposition(HouseholdInformation):
    pass


# Identity information


class Name(IdentityInformation):
    pass


class SocialSecurityNumber(IdentityInformation):
    pass


# Income information


class PreviousIncome(IncomeInformation):
    pass


class EarnedIncome(IncomeInformation):
    pass


class EmploymentIncome(EarnedIncome):
    pass


class MilitaryAllotmentIncome(EmploymentIncome):
    pass


class SelfEmploymentIncome(EmploymentIncome):
    pass


class RentIncome(EarnedIncome):
    pass


class UnearnedIncome(IncomeInformation):
    pass


class BenefitIncome(UnearnedIncome):
    pass


class DisabilityIncome(BenefitIncome):
    pass


class GIDependencyAllotment(BenefitIncome):
    pass


class PublicAssistanceGrant(BenefitIncome):
    pass


class RetirementIncome(BenefitIncome):
    pass


class PensionIncome(RetirementIncome):
    pass


class RailroadRetirementIncome(RetirementIncome):
    pass


class SocialSecurityIncome(BenefitIncome):
    pass


class SocialSecurityDependentBenefits(SocialSecurityIncome):
    pass


class SocialSecurityDisabilityIncome(SocialSecurityIncome):
    pass


class SocialSecurityRetirementBenefits(SocialSecurityIncome, RetirementIncome):
    pass


class SocialSecuritySurvivorsBenefits(SocialSecurityIncome):
    pass


class SupplementalSecurityIncome(SocialSecurityIncome):
    pass


class UnionBenefitIncome(BenefitIncome):
    pass


class VeteransIncome(BenefitIncome):
    pass


class BoarderLodgerIncome(UnearnedIncome):
    pass


class ChildSupportIncome(UnearnedIncome):
    pass


class CourtPaymentIncome(UnearnedIncome):
    pass


class EducationIncome(UnearnedIncome):
    pass


class EducationGrantIncome(EducationIncome):
    pass


class EducationLoanIncome(EducationIncome):
    pass


class FosterCareIncome(UnearnedIncome):
    pass


class GiftIncome(UnearnedIncome):
    pass


class InterestDividendRoyaltyIncome(UnearnedIncome):
    pass


class LoanIncome(UnearnedIncome):
    pass


class NoFaultInsuranceIncome(UnearnedIncome):
    pass


class PrivateDisabilityInsuranceIncome(UnearnedIncome):
    pass


class PrivatePensionAnnunityIncome(UnearnedIncome):
    pass


class SpousalSupportIncome(UnearnedIncome):
    pass


class TrainingStipendIncome(UnearnedIncome):
    pass


class TrustIncome(UnearnedIncome):
    pass


class UnemploymentInsuranceIncome(UnearnedIncome):
    pass


class WorkersCompensation(UnearnedIncome):
    pass


# Personal information


class AssistanceReceived(PersonalInformation):
    pass


class DemographicInformation(PersonalInformation):
    pass


class Age(DemographicInformation):
    pass


class LegalViolationInformation(PersonalInformation):
    pass


class FleeingFelonyLawEnforcement(LegalViolationInformation):
    pass


class FraudInformation(LegalViolationInformation):
    pass


class BuyingSellingSNAPFraud(FraudInformation):
    pass


class DuplicateSNAPBenefitFraud(FraudInformation):
    pass


class IntentionalProgramViolation(FraudInformation):
    pass


class PublicAssistanceFraudTwoOrMoreStates(FraudInformation):
    pass


class ReceivedBenefitsNotEntitledNotRepaid(FraudInformation):
    pass


class TransferredPropertyToGetBenefits(FraudInformation):
    pass


class TradingBenefitsForFirearmsDrugs(LegalViolationInformation):
    pass


class ViolatingProbationParole(LegalViolationInformation):
    pass


class MealsFromDeliveryService(PersonalInformation):
    pass


class MovedFromOtherNYCounty(PersonalInformation):
    pass


class Residence(PersonalInformation):
    pass


class ServedInMilitary(PersonalInformation):
    pass


class DependentOfMilitary(ServedInMilitary):
    pass


class SpouseServedInMilitary(ServedInMilitary):
    pass


# Relationship information


class MaritalStatus(RelationshipInformation):
    pass


class ParentRelationship(RelationshipInformation):
    pass


class AbsentParentRelationship(ParentRelationship):
    pass


class DeadParentRelationship(ParentRelationship):
    pass


# Resource information


class AnnuityResource(ResourceInformation):
    pass


class BurialResource(ResourceInformation):
    pass


class BurialFundInformation(BurialResource):
    pass


class BurialSpaceInformation(BurialResource):
    pass


class BurialTrustInformation(BurialResource):
    pass


class CashResource(ResourceInformation):
    pass


class CheckingAccountBalance(CashResource):
    pass


class CreditUnionAccountBalance(CashResource):
    pass


class RetirementAccountBalance(CashResource):
    pass


class SavingsAccountBalance(CashResource):
    pass


class InheritanceResource(ResourceInformation):
    pass


class InvestmentResource(ResourceInformation):
    pass


class BondResourceInformation(InvestmentResource):
    pass


class SavingsBondResource(BondResourceInformation):
    pass


class MutualFundInformation(InvestmentResource):
    pass


class StockResourceInformation(InvestmentResource):
    pass


class LawsuitSettlementInformation(ResourceInformation):
    pass


class LifeInsuranceResource(ResourceInformation):
    pass


class LumpSumPaymentInformation(ResourceInformation):
    pass


class RealEstateResource(ResourceInformation):
    pass


class OwnedHomeInformation(RealEstateResource):
    pass


class RealEstateInformation(RealEstateResource):
    pass


class SafeDepositBoxResource(ResourceInformation):
    pass


class TaxRefundResource(ResourceInformation):
    pass


class EarnedIncomeTaxCreditResource(TaxRefundResource):
    pass


class TransferredResourceInformation(ResourceInformation):
    pass


class TransferredTrustInformation(TransferredResourceInformation):
    pass


class TrustResource(ResourceInformation):
    pass


class InTrustAccountInformation(TrustResource):
    pass


class TrustBeneficiaryInformation(TrustResource):
    pass


class TrustFundInformation(TrustResource):
    pass


class VehicleResource(ResourceInformation):
    pass


# Shelter information


class DrugAlcoholTreatmentFacility(ShelterInformation):
    pass


class LandlordInformation(ShelterInformation):
    pass


class PublicHousingInformation(ShelterInformation):
    pass


class Section8HUDSubsidizedHousing(PublicHousingInformation):
    pass

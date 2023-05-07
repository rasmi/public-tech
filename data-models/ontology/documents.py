"""Document types."""


class Document:
    pass


class BenefitRecord(Document):
    pass


class Bill(Document):
    pass


class BusinessRecord(Document):
    pass


class CitizenshipDocument(Document):
    pass


class FinancialRecord(Document):
    pass


class IdentityDocument(Document):
    pass


class InstitutionalRecord(Document):
    pass


class InsuranceRecord(Document):
    pass


class Mail(Document):
    pass


class NewspaperRecord(Document):
    pass


class Receipt(Document):
    pass


class RelationshipDocument(Document):
    pass


class ResidenceDocument(Document):
    pass


class WrittenStatement(Document):
    pass


class VehicleRecord(Document):
    pass


# BenefitRecords


class RetirementRecord(BenefitRecord):
    pass


class PensionStatement(RetirementRecord):
    pass


class SocialSecurityLetter(BenefitRecord, WrittenStatement):
    pass


class StateDisabilityLetter(BenefitRecord, WrittenStatement):
    pass


class UnemploymentInsuranceLetter(BenefitRecord, WrittenStatement):
    pass


# Bills


class CableBill(Bill):
    pass


class PhoneBill(Bill):
    pass


class RentBill(Bill, ResidenceDocument):
    pass


class UtilityBill(Bill):
    pass


class InsuranceBill(Bill, InsuranceRecord):
    pass


class CarInsuranceBill(InsuranceBill):
    pass


class HealthInsuranceBill(InsuranceBill):
    pass


class HomeownersInsuranceBill(InsuranceBill):
    pass


class LifeInsuranceBill(InsuranceBill):
    pass


# Business records


class EmploymentRecord(BusinessRecord):
    pass


class SelfEmploymentRecord(BusinessRecord):
    pass


# Citizenship Documents


class EmploymentAuthorizationRecord(CitizenshipDocument):
    pass


class I_668BEmploymentAuthorizationDocument(EmploymentAuthorizationRecord):
    pass


class I_7668EmploymentAuthorizationDocument(EmploymentAuthorizationRecord):
    pass


class I_94ArrivalDepartureRecord(CitizenshipDocument):
    pass


class PermanentResidentCard(CitizenshipDocument):
    pass


class VisaDocument(CitizenshipDocument):
    pass


# Financial records


class BankStatement(FinancialRecord):
    pass


class BrokerageStatement(FinancialRecord):
    pass


class CreditCardStatement(Bill, FinancialRecord):
    pass


class IncomeRecord(FinancialRecord):
    pass


class Checkstub(IncomeRecord):
    pass


class EmploymentCheck(Checkstub, EmploymentRecord):
    pass


class RentalIncomeCheck(Checkstub):
    pass


class SocialSecurityCheck(BenefitRecord, Checkstub):
    pass


class StateDisabilityCheck(BenefitRecord, Checkstub):
    pass


class UnemploymentInsuranceCheck(BenefitRecord, Checkstub):
    pass


class Paystub(IncomeRecord):
    pass


class TaxRecord(FinancialRecord):
    pass


class IncomeTaxRecord(TaxRecord):
    pass


class IncomeTaxReturn(TaxRecord):
    pass


class PropertyTaxRecord(TaxRecord):
    pass


class ScheduleCQuarterlyTaxPayment(TaxRecord):
    pass


# Identity documents


class AdoptionRecord(IdentityDocument, RelationshipDocument):
    pass


class BaptismCertificate(IdentityDocument):
    pass


class BirthCertificate(IdentityDocument):
    pass


class DeathCertificate(IdentityDocument):
    pass


class DriversLicense(IdentityDocument):
    pass


class NaturalizationCertificate(CitizenshipDocument, IdentityDocument):
    pass


class Passport(CitizenshipDocument, IdentityDocument):
    pass


class ForeignPassport(Passport):
    pass


class USPassport(Passport):
    pass


class PhotoID(IdentityDocument):
    pass


class LocalID(PhotoID):
    pass


class StateID(PhotoID):
    pass


class TribalID(PhotoID):
    pass


class SocialSecurityCard(IdentityDocument):
    pass


class VoterRegistrationCard(IdentityDocument):
    pass


# Institutional records


class CensusRecord(InstitutionalRecord):
    pass


class HospitalRecord(InstitutionalRecord):
    pass


class MilitaryRecord(InstitutionalRecord):
    pass


class MilitaryID(PhotoID, MilitaryRecord):
    pass


class SchoolRecord(InstitutionalRecord):
    pass


class SocialSecurityRecord(InstitutionalRecord):
    pass


class VeteransAffairsRecord(InstitutionalRecord):
    pass


# Insurance records


class InsurancePolicy(InsuranceRecord):
    pass


class LifeInsurancePolicy(InsurancePolicy):
    pass


class MedicarePrescriptionDrugCard(InsuranceRecord):
    pass


# Mail


class USPSChangeOfAddressConfirmation(Mail):
    pass


# Receipts


class BurialReceipt(Receipt):
    pass


class RentReceipt(Receipt, ResidenceDocument):
    pass


# Relationship documents


class AdoptionRecord(IdentityDocument, RelationshipDocument):
    pass


class DivorceRecord(RelationshipDocument):
    pass


class MarriageRecord(RelationshipDocument):
    pass


# Residence documents


class Lease(ResidenceDocument):
    pass


class MortgageRecord(ResidenceDocument):
    pass


class ResidenceHistoryRecord(ResidenceDocument):
    pass


# Written statements


class ChildCareProviderStatement(WrittenStatement):
    pass


class ChildSupportEnforcementUnitStatement(WrittenStatement):
    pass


class CommunityOrganizationStatement(WrittenStatement):
    pass


class EmployerStatement(EmploymentRecord, WrittenStatement):
    pass


class FamilyCourtStatement(WrittenStatement):
    pass


class IdentityStatement(WrittenStatement, IdentityDocument):
    pass


class IncomeStatement(WrittenStatement):
    pass


class RentalIncomeStatement(IncomeStatement):
    pass


class PersonStatement(WrittenStatement):
    pass


class ChildSupportPayerStatement(PersonStatement):
    pass


class ClergyStatement(PersonStatement):
    pass


class LandlordStatement(PersonStatement):
    pass


class PhysicianStatement(PersonStatement):
    pass


class TenantStatement(PersonStatement):
    pass


class SelfStatement(PersonStatement):
    pass


class SelfIncomeStatement(IncomeStatement, SelfStatement):
    pass


class VeteransAffairsLetter(WrittenStatement):
    pass


# Vehicle records


class VehicleRegistration(VehicleRecord):
    pass


class VehicleTitle(VehicleRecord):
    pass

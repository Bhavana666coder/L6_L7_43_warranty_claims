
from warranty_claims import (
    out_of_warranty_charge,
    claim_allowed,
    sla_status
)


# 1. OUT OF WARRANTY CHARGE — BRANCH TESTS

def test_invalid_plan():
    try:
        out_of_warranty_charge("gold", 20, "defect", False)
        assert False
    except ValueError:
        assert True


def test_negative_age():
    try:
        out_of_warranty_charge("basic", -1, "defect", False)
        assert False
    except ValueError:
        assert True


def test_registered_non_premium():
    assert out_of_warranty_charge("basic", 18, "defect", True) == 0


def test_unregistered_customer():
    assert out_of_warranty_charge("basic", 13, "defect", False) == 100


def test_registered_premium():
    assert out_of_warranty_charge("premium", 37, "defect", True) == 100


def test_within_warranty_boundary():
    assert out_of_warranty_charge("basic", 12, "defect", False) == 0


def test_accidental_claim():
    assert out_of_warranty_charge("basic", 13, "accidental", False) == 200


def test_non_accidental_claim():
    assert out_of_warranty_charge("basic", 13, "defect", False) == 100


def test_excess_greater_than_12_defect():
    assert out_of_warranty_charge("basic", 25, "defect", False) == 1950


def test_excess_greater_than_12_accidental():
    assert out_of_warranty_charge("basic", 25, "accidental", False) == 3575


# 2. CLAIM ALLOWED — BRANCH TESTS

def test_recall_claim_within_limit():
    assert claim_allowed(10, 5, True) is True


def test_recall_claim_exceeds_limit():
    assert claim_allowed(10, 6, True) is False


def test_normal_claim_less_than_30_days():
    assert claim_allowed(29, 1, False) is False


def test_normal_claim_exactly_30_days():
    assert claim_allowed(30, 2, False) is True


def test_normal_claim_exceeds_limit():
    assert claim_allowed(60, 3, False) is False


# 3. SLA STATUS — BRANCH TESTS

def test_hardware_non_priority_on_track():
    assert sla_status(48, True, False) == "on_track"


def test_non_hardware_non_priority_at_risk():
    assert sla_status(12, False, False) == "at_risk"


def test_non_hardware_non_priority_critical():
    assert sla_status(11, False, False) == "critical"


def test_hardware_priority_on_track():
    assert sla_status(72, True, True) == "on_track"


def test_hardware_priority_at_risk():
    assert sla_status(60, True, True) == "at_risk"


def test_hardware_priority_critical():
    assert sla_status(35, True, True) == "critical"


def test_non_hardware_priority_on_track():
    assert sla_status(48, False, True) == "on_track"


def test_non_hardware_priority_at_risk():
    assert sla_status(36, False, True) == "at_risk"


def test_non_hardware_priority_critical():
    assert sla_status(35, False, True) == "critical"


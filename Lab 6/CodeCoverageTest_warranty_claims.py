
import pytest

from warranty_claims import (
    out_of_warranty_charge,
    claim_allowed,
    sla_status
)


# 1. OUT OF WARRANTY CHARGE TESTS

def test_invalid_plan():
    with pytest.raises(ValueError):
        out_of_warranty_charge("gold", 20, "defect", False)


def test_negative_age():
    with pytest.raises(ValueError):
        out_of_warranty_charge("basic", -1, "defect", False)


def test_within_warranty():
    assert out_of_warranty_charge("standard", 20, "defect", False) == 0


def test_registered_customer():
    assert out_of_warranty_charge("standard", 30, "defect", True) == 0


def test_defect_claim_with_small_excess():
    assert out_of_warranty_charge("basic", 13, "defect", False) == 100


def test_accidental_claim_with_large_excess():
    assert out_of_warranty_charge("basic", 37, "accidental", False) == 6875


# 2. CLAIM ALLOWED TESTS

def test_recall_claim_allowed():
    assert claim_allowed(10, 3, True) is True


def test_claim_rejected_within_30_days():
    assert claim_allowed(15, 1, False) is False


def test_claim_rejected_when_claim_limit_exceeded():
    assert claim_allowed(60, 3, False) is False


# 3. SLA STATUS TESTS

def test_sla_on_track():
    assert sla_status(60, True, False) == "on_track"


def test_sla_at_risk():
    assert sla_status(18, False, False) == "at_risk"


def test_sla_critical():
    assert sla_status(5, False, False) == "critical"


def test_sla_priority():
    assert sla_status(60, False, True) == "on_track"


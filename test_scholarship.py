import pytest
from ScholarshipEligibilityEvaluator import evaluate_scholarship, Status

# --- 1 CASO DE APPROVED ---
def test_evaluate_scholarship_approved():
    """Garante que um candidato ideal seja aprovado."""
    result = evaluate_scholarship(age=18, gpa=8.5, attendance_rate=92.0, has_required_courses=True, disciplinary_record=False)
    assert result.status == Status.APPROVED 
    assert "Applicant meets all scholarship requirements." in result.reasons 

# --- 1 CASO DE MANUAL_REVIEW ---
def test_evaluate_scholarship_manual_review_age():
    """Testa a revisão manual devido à idade menor que 18."""
    result = evaluate_scholarship(age=17, gpa=8.5, attendance_rate=90.0, has_required_courses=True, disciplinary_record=False)
    assert result.status == Status.MANUAL_REVIEW 
    assert "Applicant is under 18 and requires manual review." in result.reasons 

# --- 3 CASOS DE REJECTED (MOTIVOS DIFERENTES) ---
def test_evaluate_scholarship_rejected_age():
    """Testa rejeição por idade abaixo do mínimo."""
    result = evaluate_scholarship(age=15, gpa=8.0, attendance_rate=90.0, has_required_courses=True, disciplinary_record=False)
    assert result.status == Status.REJECTED 
    assert "Applicant is younger than the minimum age." in result.reasons 

def test_evaluate_scholarship_rejected_gpa():
    """Testa rejeição por GPA muito baixo."""
    result = evaluate_scholarship(age=20, gpa=5.9, attendance_rate=90.0, has_required_courses=True, disciplinary_record=False)
    assert result.status == Status.REJECTED 
    assert "GPA is below the minimum required." in result.reasons 

def test_evaluate_scholarship_rejected_disciplinary():
    """Testa rejeição por histórico disciplinar."""
    result = evaluate_scholarship(age=20, gpa=8.0, attendance_rate=90.0, has_required_courses=True, disciplinary_record=True)
    assert result.status == Status.REJECTED 
    assert "Applicant has a disciplinary record." in result.reasons 

# --- 2 CASOS DE ENTRADA INVÁLIDA ---
def test_evaluate_scholarship_invalid_gpa():
    """Garante que a validação de GPA dispare um erro."""
    with pytest.raises(ValueError, match="GPA must be between 0 and 10."): 
        evaluate_scholarship(age=18, gpa=11.0, attendance_rate=90.0, has_required_courses=True, disciplinary_record=False) #

def test_evaluate_scholarship_invalid_attendance():
    """Garante que a validação de presença dispare um erro."""
    with pytest.raises(ValueError, match="Attendance rate must be between 0 and 100."): 
        evaluate_scholarship(age=18, gpa=8.0, attendance_rate=105.0, has_required_courses=True, disciplinary_record=False) #[cite: 1]

# --- 4 CASOS DE VALOR LIMITE (BOUNDARY VALUES) ---
def test_evaluate_scholarship_boundary_age_16():
    """Idade 16: escapa da rejeição (<16), mas cai na revisão (<=17)."""
    result = evaluate_scholarship(age=16, gpa=8.0, attendance_rate=90.0, has_required_courses=True, disciplinary_record=False)
    assert result.status == Status.MANUAL_REVIEW 
    assert "Applicant is under 18 and requires manual review." in result.reasons 

def test_evaluate_scholarship_boundary_gpa_6_0():
    """GPA 6.0: escapa da rejeição (<6.0), mas cai na revisão (<7.0)."""
    result = evaluate_scholarship(age=20, gpa=6.0, attendance_rate=90.0, has_required_courses=True, disciplinary_record=False)
    assert result.status == Status.MANUAL_REVIEW 
    assert "GPA is in the manual review range." in result.reasons 

def test_evaluate_scholarship_boundary_attendance_75_0():
    """Presença 75.0: escapa da rejeição (<75.0), mas cai na revisão (<80.0)."""
    result = evaluate_scholarship(age=20, gpa=8.0, attendance_rate=75.0, has_required_courses=True, disciplinary_record=False)
    assert result.status == Status.MANUAL_REVIEW 
    assert "Attendance rate is in the manual review range." in result.reasons 

def test_evaluate_scholarship_boundary_attendance_80_0():
    """Presença 80.0: limite exato para escapar da revisão, resultando em aprovação."""
    result = evaluate_scholarship(age=20, gpa=8.0, attendance_rate=80.0, has_required_courses=True, disciplinary_record=False)
    assert result.status == Status.APPROVED 

def test_evaluate_scholarship_rejected_attendance():
    """Testa rejeição por taxa de presença abaixo do mínimo."""
    result = evaluate_scholarship(age=20, gpa=8.0, attendance_rate=70.0, has_required_courses=True, disciplinary_record=False)
    assert result.status == Status.REJECTED 
    assert "Attendance rate is below the minimum required." in result.reasons

def test_evaluate_scholarship_rejected_required_courses():
    """Testa rejeição por falta de cursos obrigatórios."""
    result = evaluate_scholarship(age=20, gpa=8.0, attendance_rate=90.0, has_required_courses=False, disciplinary_record=False)
    assert result.status == Status.REJECTED 
    assert "Required courses have not been completed." in result.reasons

# Depois da análise de mutantes, adicionamos mais dois casos de teste para cobrir os limites do GPA.

def test_evaluate_scholarship_boundary_gpa_10_0():
    """Mata o mutante Gt_GtE garantindo que o limite superior máximo é aceito."""
    result = evaluate_scholarship(age=20, gpa=10.0, attendance_rate=100.0, has_required_courses=True, disciplinary_record=False)
    assert result.status == Status.APPROVED 

def test_evaluate_scholarship_boundary_gpa_7_0():
    """Mata o mutante Lt_LtE garantindo que 7.0 exato resulta em aprovação, não revisão."""
    result = evaluate_scholarship(age=20, gpa=7.0, attendance_rate=90.0, has_required_courses=True, disciplinary_record=False)
    assert result.status == Status.APPROVED
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone
from django.db.models import Count
from django.db.models.functions import TruncMonth

# 👉 IMPORTA O MODEL DO APP SEPARADO
from alunos.models import Aluno

from datetime import date

def _add_months(d: date, months: int) -> date:
    y = d.year + (d.month - 1 + months) // 12
    m = (d.month - 1 + months) % 12 + 1
    return date(y, m, 1)

@login_required
def index(request):
    # KPIs
    now = timezone.localtime()
    inicio_mes = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    total_alunos = Aluno.objects.count()
    alunos_mes = Aluno.objects.filter(criado_em__gte=inicio_mes).count()

    # Série mensal (últimos 12 meses) a partir do campo criado_em
    serie_qs = (
        Aluno.objects
        .annotate(mes=TruncMonth("criado_em"))
        .values("mes")
        .annotate(qtd=Count("id"))
        .order_by("mes")
    )
    mapa = {row["mes"].date().replace(day=1): row["qtd"] for row in serie_qs}

    start = _add_months(date(now.year, now.month, 1), -11)
    labels, counts = [], []
    cursor = start
    for _ in range(12):
        labels.append(cursor.strftime("%b/%Y"))
        counts.append(mapa.get(cursor, 0))
        cursor = _add_months(cursor, 1)

    cards = [
        {"title": "Alunos (total)", "value": f"{total_alunos}"},
        {"title": "Cadastrados no mês", "value": f"{alunos_mes}"},
    ]
    return render(request, "dashboard.html", {
        "cards": cards,
        "meses_labels": labels,
        "meses_counts": counts,
    })



from django.contrib.auth import logout
from django.shortcuts import redirect


def logout_get(request):
    """
    Faz logout aceitando GET e POST e redireciona para a tela de login.
    """
    logout(request)
    return redirect('login')
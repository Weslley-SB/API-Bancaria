from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import get_db
from models.usuario import Usuario
from models.conta import Conta
from schemas import usuario
from schemas import conta

router = APIRouter(prefix="/auth", tags=["Autenticação"])

@router.post("/Registrar", response_model=usuario.UsuarioResponse)
def abrir_conta(usuario: usuario.UsuarioCreate, db: Session = Depends(get_db)):
    usuario_existente = db.query(Usuario).filter(Usuario.email == usuario.email).first()
    if usuario_existente:
        raise HTTPException(status_code=400, detail="Este email ja está cadastrado!")

    novo_usuario = Usuario(
        nome=usuario.nome,
        email=usuario.email,
        senha=usuario.senha
    )

    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)

    nova_conta = Conta(
        id_usuarios=novo_usuario.id,
        saldo = 0.0,
        numero_conta="01"
    )

    db.add(nova_conta)
    db.commit()
    db.refresh(nova_conta)

    return novo_usuario
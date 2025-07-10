from typing import Optional

from sqlalchemy import BigInteger, Double, Numeric, PrimaryKeyConstraint, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import decimal

class Base(DeclarativeBase):
    pass


class ChurnCustomers(Base):
    __tablename__ = 'churn_customers'
    __table_args__ = (
        PrimaryKeyConstraint('customerid', name='churn_customers_pkey'),
    )

    customerid: Mapped[float] = mapped_column(Double(53), primary_key=True)
    surname: Mapped[str] = mapped_column(Text)
    creditscore: Mapped[float] = mapped_column(Double(53))
    id: Mapped[Optional[int]] = mapped_column(BigInteger)
    geography: Mapped[Optional[str]] = mapped_column(Text)
    gender: Mapped[Optional[str]] = mapped_column(Text)
    age: Mapped[Optional[float]] = mapped_column(Double(53))
    tenure: Mapped[Optional[float]] = mapped_column(Double(53))
    balance: Mapped[Optional[float]] = mapped_column(Double(53))
    num_of_products: Mapped[Optional[float]] = mapped_column(Double(53))
    has_cr_card: Mapped[Optional[float]] = mapped_column(Double(53))
    is_active_member: Mapped[Optional[float]] = mapped_column(Double(53))
    estimated_salary: Mapped[Optional[float]] = mapped_column(Double(53))


class RetentionProba(Base):
    __tablename__ = 'retention_proba'
    __table_args__ = (
        PrimaryKeyConstraint('customerid', name='retention_proba_pkey'),
    )

    customerid: Mapped[float] = mapped_column(Double(53), primary_key=True)
    retentionproba: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric)

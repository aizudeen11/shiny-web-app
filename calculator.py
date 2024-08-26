import math
import pandas as pd


class Calculation:
    def __init__(
        self,
        loan_interest: float,
        loan_amount: float,
        ln_tenure: float,
        fv_interest_rate: float,
        every_rm=100,
        until_rm=1000,
        fv_n=12,
        ln_n=12,
    ):
        self.loan_interest = loan_interest
        self.loan_amount = loan_amount
        self.ln_n = ln_n
        self.ln_tenure = ln_tenure
        self.fv_interest_rate = fv_interest_rate
        self.fv_n = fv_n
        self.every_rm = every_rm
        self.until_rm = until_rm

    def loan_tenure(self, repayment: float):
        an_int = self.loan_interest / self.ln_n
        n = (
            (math.log(repayment / (repayment - self.loan_amount * an_int)))
            / (math.log(1 + an_int))
            / self.ln_n
        )
        return n

    def interest(self, ln_tenure: float):
        ttl_month = self.ln_n * ln_tenure
        repayment = (
            self.loan_amount
            * (self.loan_interest / self.ln_n)
            * ((1 + (self.loan_interest / self.ln_n)) ** ttl_month)
        ) / (((1 + (self.loan_interest / self.ln_n)) ** ttl_month) - 1)
        ttl_interest = (repayment * ttl_month) - self.loan_amount
        loan_with_interest = repayment * ttl_month
        interest_info = {
            "repayment": repayment,
            "ttl_interest": ttl_interest,
            "loan_with_interest": loan_with_interest,
        }
        return interest_info

    def future_value(self, monthly_deposit: float, fv_tenure: float):
        ttl_month = fv_tenure * self.fv_n
        fv = (
            monthly_deposit
            * (((1 + self.fv_interest_rate / self.fv_n) ** ttl_month) - 1)
            / (self.fv_interest_rate / self.fv_n)
        )
        return fv

    def compile(self):
        data, data2, data3, data4, data5 = [], [], [], [], []
        ringgit = [x for x in range(0, self.until_rm, self.every_rm)]
        repayment = self.interest(self.ln_tenure)["repayment"]
        repay_sc = [(repayment + x) for x in range(0, self.until_rm, self.every_rm)]
        for x in repay_sc:
            data2.append(self.loan_tenure(x))

        f = zip(ringgit, data2)

        for x, y in f:
            data.append(self.future_value(x, y))

        for x in data2:
            interest_info = self.interest(x)
            data3.append(interest_info["ttl_interest"])
            data4.append(interest_info["repayment"])
            data5.append(interest_info["loan_with_interest"])

        df = {
            "investment value": data,
            "loan principal": self.loan_amount,
            "total interest": data3,
            "tenure (year)": data2,
            "loan repayment": data4,
            "loan with interest": data5,
        }
        df = pd.DataFrame(df)
        df["interest deduction"] = df["total interest"][0] - df["total interest"]
        df["value"] = df["investment value"] - df["interest deduction"]
        df.index = [f"RM{x}" for x in range(0, self.until_rm, self.every_rm)]
        grf1 = df[['investment value', 'interest deduction']].plot(kind='bar', title=f'investment value vs loan interest saving on every RM{self.every_rm}').set_ylabel('in RM')
        # grf2 = df[['value']].plot(kind='bar', title=f'value on every RM{self.every_rm}').set_ylabel('in RM')
        # df = df.style.format("{:,.2f}")
        # df = df.to_dict()
        return df, grf1

    def __str__(self):
        repayments = self.interest(self.ln_tenure)
        return f"loan amount: {self.loan_amount} \nloan tenure: {self.ln_tenure} \nloan interest: {self.loan_interest} \nloan monthly repayment: {repayments['repayment']:_.2f} "

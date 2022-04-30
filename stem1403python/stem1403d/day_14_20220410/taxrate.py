"""
Tax Rate

"""


class Tax:
    def __init__(self, pst=0, province='unknown'):
        self.province = province
        self.gst = 0.05
        self.pst = pst

    def getGst(self):
        return self.gst

    def hasHst(self):
        return False

    def hasPst(self):
        return False


class TaxGST(Tax):
    def getTaxRate(self):
        return self.gst


class TaxHST(Tax):
    def __init__(self, pst, province):
        super().__init__(pst, province)
        self.hst = self.gst + self.pst

    def getTaxRate(self):
        return self.hst

    def getPst(self):
        return self.pst

    def getHst(self):
        return self.hst

    def hasHst(self):
        return True


class TaxGPST(Tax):
    def getTaxRate(self):
        return self.gst + self.pst

    def getPst(self):
        return self.pst

    def hasPst(self):
        return True


class ClientApp:
    def queryTaxRate(self, taxObj):
        print(f"{taxObj.province} sets the tax rate at {taxObj.getTaxRate():.3%}")

    def queryGst(self, taxObj):
        print(f"{taxObj.province} sets the GST rate at {taxObj.getGst():.3%}")

    def queryPst(self, taxObj):
        if taxObj.hasPst():
            print(f"{taxObj.province} sets the tax rate at {taxObj.getPst():.3%}")
        else:
            print(f"{taxObj.province} has no PST.")

    def queryHst(self, taxObj):
        if taxObj.hasHst():
            print(f"{taxObj.province} sets the tax rate at {taxObj.getHst():.3%}")
        else:
            print(f"{taxObj.province} has no HST.")


#
app = ClientApp()

# Quebec
qcTax = TaxGPST(0.09975, 'Quebec')
app.queryTaxRate(qcTax)
app.queryGst(qcTax)
app.queryPst(qcTax)
app.queryHst(qcTax)
print()

# Ontario
onTax = TaxHST(0.08, 'Ontario')
app.queryTaxRate(onTax)
app.queryGst(onTax)
app.queryPst(onTax)
app.queryHst(onTax)
print()

# Alberta
abTax = TaxGST(province='Alberta')
app.queryTaxRate(abTax)
app.queryGst(abTax)
app.queryPst(abTax)
app.queryHst(abTax)
print()

# BC
bcTax = TaxGPST(0.07, 'British Columbia')
app.queryTaxRate(bcTax)
app.queryGst(bcTax)
app.queryPst(bcTax)
app.queryHst(bcTax)


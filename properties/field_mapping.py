"""This module is field mapping"""

"""mapping for basic info"""
def get_basic_info_field_mapping():
    basic_info_field_mapping = {
        "Result": {
            "Name": {
                "Name03": {
                    "@value": "PatientLastName__c"
                },
                "Name04": {
                    "@value": "PatientFirstName__c"
                },
                "Name05": {
                    "@value": "PatientMiddleName__c"
                },
                "Name09": {
                    "@value": "MBI__c"
                }
            },
            "Address": {
                "Address01": {
                    "@value": "Address1__c"
                }
            },
            "Address2": {
                "Address201": {
                    "@value": "City__c"
                },
                "Address202": {
                    "@value": "State__c"
                },
                "Address203": {
                    "@value": "Zipcode__c"
                }
            },
            "Stats": {
                "Stats02": {
                    "@value": "DOB__c"
                },
                "Stats03": {
                    "@value": "Sex__c"
                }
            }
        }
    }
    return basic_info_field_mapping


def get_basic_info_condition_field_mapping():
    return {
        "Result": {
            "Section": {
                "Date": {
                    "Date03": {
                        "@value": "StartDate"
                    }
                },
                "Eligibility": {
                    "Eligibility03": {
                        "@value": "Part A"
                    }
                }
            }
        }
    }


def get_inpatient_field_mapping():
    return {
    }


def get_deductible_caps_field_mapping():
    return {
        # "Result": {
        #     "Section": {
        #         "Eligibility": {
        #             "Eligibility01": {
        #                 "@value": "Deductible"
        #             },
        #             "Eligibility03": {
        #                 "@value": "Plan Waiting Period"
        #             },
        #             "Eligibility04": {
        #                 "@value": "Medicare Part B"
        #             },
        #             "Eligibility06": {
        #                 "@value": "Remaining"
        #             }
        #         },
        #         "Date": {
        #             "Date03": {
        #                 "@value": "20210101-20211231"
        #             }
        #         }
        #     }
        # }
    }


def get_qmb_field_mapping():
    return {
        "Result": {
            "Section": {
                "Eligibility": {
                    "Eligibility05": {
                        "@value": "QmbState__c"
                    }
                }
            }
        }
    }


def get_msp_static_field_mapping():
    return {
        "Result": {
            "Section": {
                "Address": {
                    "Address01": {
                        "@value": "MspAddress1__c"
                    }
                },
                "Address2": {
                    "Address201": {
                        "@value": "MspCity__c"
                    },
                    "Address202": {
                        "@value": "MspState__c"
                    },
                    "Address203": {
                        "@value": "MspZip__c"
                    }
                }
            }
        }
    }


def get_msp_conditional_field_mapping():
    return {
        "Result": {
            "Section": {
                "Date": {
                    "Date03": {
                        "@value": "20120101-20181031"
                    }
                },
                "Eligibility": {
                    "Eligibility01": {
                        "@value": "Other or Additional Payor"
                    },
                    "Eligibility03": {
                        "@value": "Plan Waiting Period"
                    },
                    "Eligibility04": {
                        "@value": "MSPType__c"
                    }
                }
            }
        }
    }


def get_plan_coverage_static_field_mapping():
    return {
        "Result": {
            "Section": {
                "Info": [
                    {
                        "Info02": {
                            "@value": "Contract__c"
                        }
                    },
                    {
                        "Info03": {
                            "@value": "PlanName__c"
                        }
                    }
                ],
                "MoreDetails": {
                    "Name": {
                        "Name03": {
                            "@value": "ContractName__c"
                        }
                    },
                    "Address": {
                        "Addresse01": {
                            "@value": "PlanCoverageAddress__c"
                        }
                    },
                    "Address2": {
                        "Address201": {
                            "@value": "PlanCoverageCity__c"
                        },
                        "Address202": {
                            "@value": "PlanCoverageState__c"
                        },
                        "Address203": {
                            "@value": "PlanCoverageZipcode__c"
                        }
                    },
                    "Contact": {
                        "Contact04": {
                            "@value": "Phone__c"
                        },
                        "Contact06": {
                            "@value": "PlanCoverageURL__c"
                        }
                    }
                }
            }
        }
    }


def get_plan_coverage_conditional_field_mapping():
    return {
        "Result": {
            "Section": {
                "Eligibility": {
                    "Eligibility04": {
                        "@value": ['HMO Non-Risk', 'HMO Medicare Risk', 'Indemnity', 'PPO', 'POS']
                    }
                },
                "Date": {
                    "Date03": {
                        "@value": "20120101-20181031"
                    }
                }

            }
        }
    }


def get_part_d_static_field_mapping():
    return {
        "Result": {
            "Section": {
                "MoreDetails": {
                    "Address": {
                        "Addresse01": {
                            "@value": "PartDAddress1__c"
                        }
                    },
                    "Address2": {
                        "Address201": {
                            "@value": "PartDCity__c"
                        },
                        "Address202": {
                            "@value": "PartDState__c"
                        },
                        "Address203": {
                            "@value": "PartDZipcode__c"
                        }
                    },
                    "Contact": {
                        "Contact04": {
                            "@value": "PartDPhone__c"
                        },
                        "Contact06": {
                            "@value": "PartDURL__c"
                        }
                    }
                }
            }
        }
    }


def get_part_d_conditional_field_mapping():
    return {
        "Result": {
            "Section": {
                "Eligibility": {
                    "Eligibility04": {
                        "@value": "Medicare Part D"
                    }
                },
                "Date": {
                    "Date03": {
                        "@value": "20120101-20181031"
                    }
                },
                "Info": [
                    {
                        "Info02": {
                            "@value": "ContractNumber"
                        }
                    },
                    {
                        "Info03": {
                            "@value": "PlanName"
                        }
                    }
                ]

            }
        }
    }


def get_error_mapping():
    return {
        "Result": {
            "Section": {
                "Error": {
                    "Error03": {
                        "@value": "Error_Reason"
                    }

                }

            }
        }
    }

def get_snf_conditional_mapping():
    return {
        "Result": {
            "Section": {
                "Eligibility": {
                    "Eligibility04": {
                        "@value": "Medicare Part A"
                    },
                    "Eligibility01": {
                        "@value": "Benefit Description"
                    }
                },
                "Date": {
                    "Date03": {
                        "@value": "20120101-20181031"
                    }
                },
            }
        }
    }

def get_snf_static_mapping():
    return {
        "Result": {
            "Section": {
                "Eligibility": {
                    "Eligibility03": {
                        "@value": "Snf_VisitType__c"
                    }
                },
                "MoreDetails": {
                    "Name": {
                        "Name09": {
                            "@value": "Snf_BillingNPI__c"
                        }
                    }
                }
            }
        }
    }

def get_home_health_conditional_mapping():
    return {
        "Result": {
            "Section": {
                "Eligibility": {
                    "Eligibility03": {
                        "@value": "Contains 'Home Health Care'"
                    },

                },
                "Date": {
                    "Date03": {
                        "@value": "20120101-20181031"
                    }
                }
            }
        }
    }

def get_home_health_static_mapping():
    return {
        "Result": {
            "Section": {
                "MoreDetails": {
                    "Name": {
                        "Name09": {
                            "@value": "HH_NPI__c"
                        }
                    }
                },
                "Note":{
                    "Note01": {
                        "@value": "HH_PatientStatus__c"
                    }
                }
            }
        }
    }

def get_hospice_conditional_field_mapping():
    return {
        "Result": {
            "Section": {
                "Eligibility": {
                    "Eligibility03": {
                        "@value": "Contains 'Hospice'"
                    },

                },
                "Date": {
                    "Date03": {
                        "@value": "20120101-20181031"
                    }
                },
                "Note": {
                    "Note01": {
                        "@value": "revoc code"
                    }
                }
            }
        }
    }

def get_hospice_static_field_mapping():
    return {
        "Result": {
            "Section": {
                "MoreDetails": {
                    "Name": {
                        "Name09": {
                            "@value": "HospiceNPI__c"
                        }
                    }
                },
                "Service": {
                    "Service02": {
                        "@value": "DaysUsed__c"
                    }
                }
            }
        }
    }


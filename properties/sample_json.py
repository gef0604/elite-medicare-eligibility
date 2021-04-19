snf_sample_json = {
        "Result": {
            "Section": {
                "Eligibility": {
                    "Eligibility04": {
                        "@value": "Medicare Part A"
                    },
                    "Eligibility01": {
                        "@value": "Benefit Description"
                    },
                    "Eligibility03": {
                        "@value": "Test Type"
                    }

                },
                "MoreDetails": {
                    "Name": {
                        "Name09": {
                            "@value": "testnpi"
                        }
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

hh_sample_json = {
        "Result": {
            "Section": {
                "Eligibility": {
                    "Eligibility03": {
                        "@value": "Contains 'Home Health Care'"
                    }
                },
                "Date": {
                    "Date03": {
                        "@value": "20120101-20181031"
                    }
                },
                "MoreDetails": {
                    "Name": {
                        "Name09": {
                            "@value": "123123123123"
                        }
                    }
                },
                "Note":{
                    "Note01": {
                        "@value": "test status"
                    }
                }
            }
        }
    }

hospice_sample_json = {
        "Result": {
            "Section": {
                "MoreDetails": {
                    "Name": {
                        "Name09": {
                            "@value": "123123123321"
                        }
                    }
                },
                "Service": {
                    "Service02": {
                        "@value": "25"
                    }
                },
                "Eligibility": {
                    "Eligibility03": {
                        "@value": "Hospice 123"
                    }
                },
                "Date": {
                    "Date03": {
                        "@value": "20120101-20181031"
                    }
                },
                "Note": {
                    "Note01": {
                        "@value": "1"
                    }
                }
            }
        }
    }

part_sample_json =  {
  "Result": {
    "Section": {
      "Eligibility": {
        "Eligibility01": {
          "@value": "Other or Additional Payor"
        },
        "Eligibility03": {
          "@value": "Pharmacy"
        },
        "Eligibility04": {
          "@value": "Other"
        }
      },
      "Info": [
        {
          "Info01": {
            "@value": "Plan Number"
          },
          "Info02": {
            "@value": "H0123"
          }
        },
        {
          "Info01": {
            "@value": "Plan Network Identification Number"
          },
          "Info02": {
            "@value": "000"
          },
          "Info03": {
            "@value": "Acme Example"
          }
        }
      ],
      "Date": {
        "Date01": {
          "@value": "Benefit"
        },
        "Date02": {
          "@value": "Date Expressed in Format CCYYMMDD"
        },
        "Date03": {
          "@value": "20210101"
        }
      },
      "MoreDetails": {
        "Name": {
          "Name01": {
            "@value": "Payer"
          },
          "Name02": {
            "@value": "Non-Person Entity"
          },
          "Name03": {
            "@value": "ACME, INC."
          }
        },
        "Address": {
          "Address01": {
            "@value": "100 MAIN AVE"
          },
          "Address02": {
            "@value": "Ren 1"
          }
        },
        "Address2": {
          "Address201": {
            "@value": "Tampa"
          },
          "Address202": {
            "@value": "FL"
          },
          "Address203": {
            "@value": "33634"
          }
        },
        "Contact": {
          "Contact01": {
            "@value": "Information Contact"
          },
          "Contact03": {
            "@value": "Telephone"
          },
          "Contact04": {
            "@value": "8880001234"
          },
          "Contact05": {
            "@value": "Uniform Resource Locator (URL)"
          },
          "Contact06": {
            "@value": "www.example.com/medicare"
          }
        }
      }
    }
  }
}

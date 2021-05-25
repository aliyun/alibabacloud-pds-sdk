// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.PDS.Client.Models
{
    /**
     * 
     */
    public class AuthConfig : TeaModel {
        [NameInMap("app_id")]
        [Validation(Required=false)]
        public string AppId { get; set; }

        [NameInMap("app_secret")]
        [Validation(Required=false)]
        public string AppSecret { get; set; }

        [NameInMap("callback_security")]
        [Validation(Required=false)]
        public bool? CallbackSecurity { get; set; }

        [NameInMap("enable")]
        [Validation(Required=false)]
        public bool? Enable { get; set; }

        [NameInMap("endpoint")]
        [Validation(Required=false)]
        public string Endpoint { get; set; }

        [NameInMap("enterprise_id")]
        [Validation(Required=false)]
        public string EnterpriseId { get; set; }

        [NameInMap("ldap_config")]
        [Validation(Required=false)]
        public LdapConfig LdapConfig { get; set; }

        [NameInMap("login_page_headers")]
        [Validation(Required=false)]
        public Dictionary<string, object> LoginPageHeaders { get; set; }

        [NameInMap("login_page_template")]
        [Validation(Required=false)]
        public string LoginPageTemplate { get; set; }

        [NameInMap("login_page_vars")]
        [Validation(Required=false)]
        public Dictionary<string, object> LoginPageVars { get; set; }

        [NameInMap("white_list_config")]
        [Validation(Required=false)]
        public Dictionary<string, object> WhiteListConfig { get; set; }

        [NameInMap("white_list_enable")]
        [Validation(Required=false)]
        public bool? WhiteListEnable { get; set; }

    }

}

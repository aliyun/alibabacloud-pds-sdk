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
    public class LdapConfig : TeaModel {
        [NameInMap("admin_dn")]
        [Validation(Required=false)]
        public string AdminDn { get; set; }

        [NameInMap("admin_password")]
        [Validation(Required=false)]
        public string AdminPassword { get; set; }

        [NameInMap("base_dn")]
        [Validation(Required=false)]
        public string BaseDn { get; set; }

        [NameInMap("host")]
        [Validation(Required=false)]
        public string Host { get; set; }

        [NameInMap("port")]
        [Validation(Required=false)]
        public long? Port { get; set; }

        [NameInMap("uid")]
        [Validation(Required=false)]
        public string Uid { get; set; }

    }

}

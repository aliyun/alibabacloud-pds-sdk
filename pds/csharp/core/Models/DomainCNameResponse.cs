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
    public class DomainCNameResponse : TeaModel {
        /// <summary>
        /// data cname list
        /// </summary>
        [NameInMap("data_cname_list")]
        [Validation(Required=true)]
        public List<DataCName> DataCnameList { get; set; }

        /// <summary>
        /// domain ID
        /// </summary>
        [NameInMap("domain_id")]
        [Validation(Required=true)]
        public string DomainId { get; set; }

    }

}

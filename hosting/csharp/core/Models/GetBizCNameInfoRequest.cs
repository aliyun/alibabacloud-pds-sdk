// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.Hosting.Client.Models
{
    /**
     * 
     */
    public class GetBizCNameInfoRequest : TeaModel {
        /// <summary>
        /// cname type
        /// </summary>
        [NameInMap("cname_type")]
        [Validation(Required=true)]
        public string CnameType { get; set; }

        /// <summary>
        /// domain ID
        /// </summary>
        [NameInMap("domain_id")]
        [Validation(Required=true)]
        public string DomainId { get; set; }

        /// <summary>
        /// is vpc
        /// </summary>
        [NameInMap("is_vpc")]
        [Validation(Required=false)]
        public bool? IsVpc { get; set; }

    }

}

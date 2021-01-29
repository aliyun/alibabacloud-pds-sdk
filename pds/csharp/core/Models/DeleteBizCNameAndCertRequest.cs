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
    public class DeleteBizCNameAndCertRequest : TeaModel {
        /// <summary>
        /// api cname
        /// </summary>
        [NameInMap("biz_cname")]
        [Validation(Required=false)]
        public string BizCname { get; set; }

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
        /// vpc
        /// </summary>
        [NameInMap("is_vpc")]
        [Validation(Required=false)]
        public bool? IsVpc { get; set; }

    }

}

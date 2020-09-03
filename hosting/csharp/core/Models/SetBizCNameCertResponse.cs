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
    public class SetBizCNameCertResponse : TeaModel {
        /// <summary>
        /// biz cname
        /// </summary>
        [NameInMap("biz_cname")]
        [Validation(Required=false)]
        public string BizCname { get; set; }

        /// <summary>
        /// cert name
        /// </summary>
        [NameInMap("cert_name")]
        [Validation(Required=false)]
        public string CertName { get; set; }

        /// <summary>
        /// cname type
        /// </summary>
        [NameInMap("cname_type")]
        [Validation(Required=false)]
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

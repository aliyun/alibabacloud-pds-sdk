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
    public class SetBizCNameCertRequest : TeaModel {
        [NameInMap("CertID")]
        [Validation(Required=false)]
        public string CertID { get; set; }

        /// <summary>
        /// biz cname
        /// </summary>
        [NameInMap("biz_cname")]
        [Validation(Required=false)]
        public string BizCname { get; set; }

        /// <summary>
        /// cert body
        /// </summary>
        [NameInMap("cert_body")]
        [Validation(Required=true)]
        public string CertBody { get; set; }

        /// <summary>
        /// cert name
        /// </summary>
        [NameInMap("cert_name")]
        [Validation(Required=true)]
        public string CertName { get; set; }

        /// <summary>
        /// cert privatekey
        /// </summary>
        [NameInMap("cert_privatekey")]
        [Validation(Required=true)]
        public string CertPrivatekey { get; set; }

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
        /// biz cname
        /// </summary>
        [NameInMap("is_vpc")]
        [Validation(Required=false)]
        public bool? IsVpc { get; set; }

    }

}

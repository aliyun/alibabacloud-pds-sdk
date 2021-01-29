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
    public class SetDataCNameRequest : TeaModel {
        /// <summary>
        /// cn-shanghai data cname
        /// </summary>
        [NameInMap("data_cname")]
        [Validation(Required=true)]
        public string DataCname { get; set; }

        /// <summary>
        /// domain ID
        /// </summary>
        [NameInMap("domain_id")]
        [Validation(Required=true)]
        public string DomainId { get; set; }

        /// <summary>
        /// location
        /// </summary>
        [NameInMap("location")]
        [Validation(Required=true)]
        public string Location { get; set; }

    }

}

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
    public class SetDataCNameResponse : TeaModel {
        /// <summary>
        /// datacname
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
        /// data location
        /// </summary>
        [NameInMap("location")]
        [Validation(Required=true)]
        public string Location { get; set; }

    }

}

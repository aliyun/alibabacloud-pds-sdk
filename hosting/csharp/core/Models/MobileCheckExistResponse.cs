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
    public class MobileCheckExistResponse : TeaModel {
        /// <summary>
        /// 当前手机号是否存在
        /// </summary>
        [NameInMap("is_exist")]
        [Validation(Required=true)]
        public bool? IsExist { get; set; }

        /// <summary>
        /// 待查询的手机号
        /// </summary>
        [NameInMap("phone_number")]
        [Validation(Required=true)]
        public string PhoneNumber { get; set; }

        /// <summary>
        /// 国家编号，默认86，不需要填+号，直接填数字
        /// </summary>
        [NameInMap("phone_region")]
        [Validation(Required=false)]
        public string PhoneRegion { get; set; }

    }

}

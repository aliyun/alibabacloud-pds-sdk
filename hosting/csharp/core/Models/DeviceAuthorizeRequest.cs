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
    public class DeviceAuthorizeRequest : TeaModel {
        /// <summary>
        /// Client ID, 此处填写创建App时返回的AppID
        /// </summary>
        [NameInMap("ClientID")]
        [Validation(Required=true)]
        public string ClientID { get; set; }

        /// <summary>
        /// 设备信息，用于用户识别设备
        /// </summary>
        [NameInMap("DeviceInfo")]
        [Validation(Required=false)]
        public string DeviceInfo { get; set; }

        /// <summary>
        /// 设备名，实现方需保证不同设备的设备名不重复（推荐用硬件名称+硬件型号作为设备名）
        /// </summary>
        [NameInMap("DeviceName")]
        [Validation(Required=true)]
        public string DeviceName { get; set; }

        /// <summary>
        /// 鉴权方式，目前支持ding,ram鉴权
        /// </summary>
        [NameInMap("LoginType")]
        [Validation(Required=false)]
        public string LoginType { get; set; }

        /// <summary>
        /// 申请的权限列表, 默认为所有权限
        /// </summary>
        [NameInMap("Scope")]
        [Validation(Required=false)]
        public List<string> Scope { get; set; }

    }

}

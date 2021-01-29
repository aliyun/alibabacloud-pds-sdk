<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * get_share_id request
 */
class GetShareLinkIDRequest extends Model {
    protected $_name = [
        'shareMsg' => 'share_msg',
    ];
    public function validate() {}
    public function toMap() {
        $res = [];
        if (null !== $this->headers) {
            $res['headers'] = $this->headers;
        }
        if (null !== $this->shareMsg) {
            $res['share_msg'] = $this->shareMsg;
        }
        return $res;
    }
    /**
     * @param array $map
     * @return GetShareLinkIDRequest
     */
    public static function fromMap($map = []) {
        $model = new self();
        if(isset($map['headers'])){
            $model->headers = $map['headers'];
        }
        if(isset($map['share_msg'])){
            $model->shareMsg = $map['share_msg'];
        }
        return $model;
    }
    public $headers;

    /**
     * @description share_msg
     * @example 复制这段话¢oJ311MvRD8R¢打開阿里云宝App【来自xxx的分享】
     * @var string
     */
    public $shareMsg;

}

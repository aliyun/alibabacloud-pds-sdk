<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * *
 */
class SetBizCNameCertResponse extends Model {
    protected $_name = [
        'bizCname' => 'biz_cname',
        'certName' => 'cert_name',
        'cnameType' => 'cname_type',
        'domainId' => 'domain_id',
        'isVpc' => 'is_vpc',
    ];
    public function validate() {
        Model::validateRequired('domainId', $this->domainId, true);
    }
    public function toMap() {
        $res = [];
        if (null !== $this->bizCname) {
            $res['biz_cname'] = $this->bizCname;
        }
        if (null !== $this->certName) {
            $res['cert_name'] = $this->certName;
        }
        if (null !== $this->cnameType) {
            $res['cname_type'] = $this->cnameType;
        }
        if (null !== $this->domainId) {
            $res['domain_id'] = $this->domainId;
        }
        if (null !== $this->isVpc) {
            $res['is_vpc'] = $this->isVpc;
        }
        return $res;
    }
    /**
     * @param array $map
     * @return SetBizCNameCertResponse
     */
    public static function fromMap($map = []) {
        $model = new self();
        if(isset($map['biz_cname'])){
            $model->bizCname = $map['biz_cname'];
        }
        if(isset($map['cert_name'])){
            $model->certName = $map['cert_name'];
        }
        if(isset($map['cname_type'])){
            $model->cnameType = $map['cname_type'];
        }
        if(isset($map['domain_id'])){
            $model->domainId = $map['domain_id'];
        }
        if(isset($map['is_vpc'])){
            $model->isVpc = $map['is_vpc'];
        }
        return $model;
    }
    /**
     * @description biz cname
     * @example api.yoursite.com
     * @var string
     */
    public $bizCname;

    /**
     * @description cert name
     * @example xdrv2020cert
     * @var string
     */
    public $certName;

    /**
     * @description cname type
     * @example api
     * @var string
     */
    public $cnameType;

    /**
     * @description domain ID
     * @example sz100
     * @var string
     */
    public $domainId;

    /**
     * @description is vpc
     * @example false
     * @var bool
     */
    public $isVpc;

}
